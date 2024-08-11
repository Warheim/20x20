from backend.download_archive.download_file import DownloadArchive
from backend.engine_module.config_handler import ConfigSite

if __name__ == '__main__':
    cfg_site = ConfigSite()
    download_scheme = DownloadArchive(cfg_site.link, cfg_site.file_name, cfg_site.encoding)
    download_scheme.page_download()
