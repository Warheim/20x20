from backend.download_archive.download_file import DownloadArchive
from backend.engine_module.config_handler import ConfigForSite, ConfigForParser
from backend.parse_archive.parse import ParseArchive

# TODO find the way to give args more compressed
if __name__ == '__main__':
    cfg_site = ConfigForSite()
    cfg_parser = ConfigForParser()
    download_scheme = DownloadArchive(
        cfg_site.link, cfg_site.file_name, cfg_site.encoding)
    download_scheme.page_download()

    parse_scheme = ParseArchive(cfg_parser.tag, cfg_parser.main_class, cfg_parser.run_class, cfg_parser.dt_class,
                                cfg_parser.nums_class, cfg_parser.encoding, cfg_parser.file_name)
    soup = parse_scheme.soup()
    data = parse_scheme.parse(soup)
    clean_data = parse_scheme.clean_data(data)

    # lst_a = []
    # lst_b = []
    #
    # for run in clean_data:
    #     for num in run[3]:
    #         if num not in lst_a:
    #             lst_a.append(num)
    #
    # for run in clean_data:
    #     for num in run[4]:
    #         if num not in lst_b:
    #             lst_b.append(num)
    #
    # print(lst_a[-4:])
    # print(lst_b[-4:])
