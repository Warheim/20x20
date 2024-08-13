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
    # download_scheme.page_download()

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

    pairs_a = analyze.count_nums_pairs(analyze.win_nums_boxes_a)
    pairs_b = analyze.count_nums_pairs(analyze.win_nums_boxes_b)

    summary_a = analyze.summary_nums_count(popularity_a, stagnation_a, pairs_a)
    summary_b = analyze.summary_nums_count(popularity_b, stagnation_b, pairs_b)

    organizer_a = analyze.organizer_for_pairs(summary_a)
    organizer_b = analyze.organizer_for_pairs(summary_b)

    res_a_sorted = sorted(organizer_a.items(), key=lambda x: x[1], reverse=True)
    res_b_sorted = sorted(organizer_b.items(), key=lambda x: x[1], reverse=True)

    clean_numbers_a = analyze.clean_nums(res_a_sorted)
    clean_numbers_b = analyze.clean_nums(res_b_sorted)

    print(clean_numbers_a)
    print(clean_numbers_b)
