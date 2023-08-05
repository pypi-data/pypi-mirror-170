# Copyright (c) Kuba Szczodrzyński 2022-07-29.

from bk7231tools.serial import BK7231Serial

from uf2tool import UploadContext


# noinspection PyUnusedLocal
def upload(
    ctx: UploadContext,
    port: str,
    baud: int = None,
    timeout: float = None,
    **kwargs,
):
    # collect continuous blocks of data (before linking, as this takes time)
    parts = ctx.collect(ota_idx=1)

    prefix = "|   |--"
    baudrate = baud or ctx.baudrate or 115200
    print(prefix, f"Trying to link on {port} @ {baudrate}")
    # connect to chip
    bk = BK7231Serial(port=port, baudrate=baudrate, link_timeout=timeout or 10.0)

    # write blocks to flash
    for offs, data in parts.items():
        length = len(data.getvalue())
        data.seek(0)
        print(prefix, f"Writing {length} bytes to 0x{offs:06x}")
        try:
            bk.program_flash(
                data,
                length,
                offs,
                verbose=False,
                crc_check=True,
                dry_run=False,
                really_erase=True,
            )
        except ValueError as e:
            raise RuntimeError(f"Writing failed: {e.args[0]}")
    # reboot the chip
    bk.reboot_chip()
