from backend.download_archive.download_file import DownloadArchive
from backend.engine_module.config_handler import ConfigForSite, ConfigForParser
from backend.parse_archive.parse import ParseArchive
from backend.analyze_archive.analyze import AnalyzeNums

# TODO find the way to give args more compressed
if __name__ == '__main__':
    cfg_site = ConfigForSite()
    cfg_parser = ConfigForParser()

    download_scheme = DownloadArchive(
        cfg_site.link, cfg_site.file_name, cfg_site.encoding)
    download_scheme.page_download()
    #
    # parse_scheme = ParseArchive(cfg_parser.tag, cfg_parser.main_class, cfg_parser.run_class, cfg_parser.dt_class,
    #                             cfg_parser.nums_class, cfg_parser.encoding, cfg_parser.file_name)
    # soup = parse_scheme.soup()
    # data = parse_scheme.parse(soup)
    # clean_data = parse_scheme.clean_data(data)
    #
    # analyze = AnalyzeNums.analyze_nums(clean_data)
    # print(analyze)
