from download_archive.download_file import DownloadArchive
from config_management.config_management import ConfigBigSportLoto
from parse_archive.parse import ParseArchive
# from analyze_archive.analyze import AnalyzeNums

# TODO find the way to give args more compressed
if __name__ == '__main__':
    cfg_BigSportLoto = ConfigBigSportLoto()

    download_scheme = DownloadArchive(
        cfg_BigSportLoto.link, cfg_BigSportLoto.file_name, cfg_BigSportLoto.encoding)
    download_scheme.page_download()
    parse_scheme = ParseArchive()
    soup = parse_scheme.soup()
    data = parse_scheme.parse(soup)
    clean_data = parse_scheme.clean_data(data)
    print(clean_data)
    #
    # analyze = AnalyzeNums.analyze_nums(clean_data)
    # print(analyze)
