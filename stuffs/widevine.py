import os
import shutil
from stuffs.general import General
from tools.helper import run
from tools.logger import Logger


class Widevine(General):
    partition = "vendor"
    dl_link = "https://codeload.github.com/supremegamers/vendor_google_proprietary_widevine-prebuilt/zip/94c9ee172e3d78fecc81863f50a59e3646f7a2bd"
    dl_file_name = "widevine.zip"
    extract_to = "/tmp/widevineunpack"
    act_md5 = "a31f325453c5d239c21ecab8cfdbd878"
    files = [
            "bin/hw/android.hardware.drm@1.3-service-lazy.widevine",
            "bin/move_widevine_data.sh",
            "etc/init/android.hardware.drm@1.3-service-lazy.widevine.rc",
            "etc/vintf/manifest/manifest_android.hardware.drm@1.3-service.widevine.xml",
            "lib/libwvhidl.so",
            "lib/mediadrm",
            "lib64/mediadrm"
        ]

    def copy(self):
        run(["chmod", "+x", self.extract_to, "-R"])
        Logger.info("Copying widevine library files ...")
        shutil.copytree(os.path.join(self.extract_to, "vendor_google_proprietary_widevine-prebuilt-94c9ee172e3d78fecc81863f50a59e3646f7a2bd",
                        "prebuilts"), os.path.join(self.copy_dir, self.partition), dirs_exist_ok=True)
