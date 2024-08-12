from collections import Counter
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

    parse_scheme = ParseArchive(cfg_parser.tag, cfg_parser.main_class, cfg_parser.run_class, cfg_parser.dt_class,
                                cfg_parser.nums_class, cfg_parser.encoding, cfg_parser.file_name)
    soup = parse_scheme.soup()
    data = parse_scheme.parse(soup)
    clean_data = parse_scheme.clean_data(data)
    analyze = AnalyzeNums(clean_data)
    popularity_a = analyze.count_nums_popularity(analyze.win_nums_a)
    popularity_b = analyze.count_nums_popularity(analyze.win_nums_b)
    stagnation_a = analyze.count_nums_stagnation(analyze.win_nums_boxes_a)
    stagnation_b = analyze.count_nums_stagnation(analyze.win_nums_boxes_b)

    # TODO organize the code below
    res_a = dict(Counter(popularity_a) + Counter(stagnation_a))
    res_b = dict(Counter(popularity_b) + Counter(stagnation_b))
    res_a_sorted = sorted(res_a.items(), key=lambda x: x[1], reverse=True)
    res_b_sorted = sorted(res_b.items(), key=lambda x: x[1], reverse=True)
