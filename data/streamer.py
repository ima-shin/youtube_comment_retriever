from enum import Enum


class Streamer(Enum):
    """
    ライバー情報
    {
        :gender 0:   性別（基本見た目から決定。公式設定があるものはそちらを優先） 0->female, 1->male, 2->other
        :channel_id  チャンネルID
    }
    """
    KUZUHA = {"name": "葛葉", "gender": 1, "channel_id": "UCSFCh5NL4qXrAy9u-u2lX3g"}
    KANAE = {"name": "叶", "gender": 1, "channel_id": "UCspv01oxUFf_MTSipURRhkA"}
    MITO_TSUKINO = {"name": "月ノ美兎", "gender": 0, "channel_id": "UCD-miitqNY3nyukJ4Fnf4_A"}
    HIMAWARI_HONMA = {"name": "本間ひまわり", "gender": 0, "channel_id": "UC0g1AE0DOjBYnLhkgoRWN1w"}
    RYUSHEN = {"name": "緑仙", "gender": 2, "channel_id": "UCt5-0i4AVHXaWJrL8Wql3mw"}
    CHIHIRO_YUKI = {"name": "勇気ちひろ", "gender": 0, "channel_id": "UCLO9QDxVL4bnvRRsz6K4bsQ"}
    SAKU_SASAKI = {"name": "笹木咲", "gender": 0, "channel_id": "UCoztvTULBYd3WmStqYeoHcA"}
    YUIKA_SINA = {"name": "椎名唯華", "gender": 0, "channel_id": "UC_4tXjqecqox5Uc05ncxpxg"}
    UTAKO_SUZUKA = {"name": "鈴鹿詩子", "gender": 0, "channel_id": "UCwokZsOK_uEre70XayaFnzA"}
    KIZUKU_YASHIRO = {"name": "社築", "gender": 1, "channel_id": "UCKMYISTJAQ8xTplUPHiABlA"}
    MINATO_FUWA = {"name": "不破湊", "gender": 1, "channel_id": "UC6wvdADTJ88OfIbJYIpAaDA"}
    LULU_SUZUHARA = {"name": "鈴原るる", "gender": 0, "channel_id": "UC_a1ZYZ8ZTXpjg9xUY9sj8w"}
    ARS_ALMAL = {"name": "アルス・アルマル", "gender": 0, "channel_id": "UCdpUojq0KWZCN9bxXnZwz5w"}
    HAYATO_KAGAMI = {"name": "加賀美ハヤト", "gender": 1, "channel_id": "UCmovZ2th3Sqpd00F5RdeigQ"}
    MELISSA_KINRENKA = {"name": "メリッサ・キンレンカ", "gender": 2, "channel_id": "UCwcyyxn6h9ex4sMXGtpQE_g"}
    KAI_MAYUZUMI = {"name": "黛灰", "gender": 1, "channel_id": "UCb5JxV6vKlYVknoJB8TnyYg"}
    RION_TAKAMIYA = {"name": "鷹宮リオン", "gender": 0, "channel_id": "UCV5ZZlLjk5MKGg3L0n0vbzw"}
    TOYA_KENMOCHI = {"name": "剣持刀也", "gender": 1, "channel_id": "UCv1fFr156jc65EMiLbaLImw"}
    SARA_HOSHIKAWA = {"name": "星川サラ", "gender": 0, "channel_id": "UC9V3Y3_uzU5e-usObb6IE1w"}
    NUI_SOCIERE = {"name": "ニュイ・ソシエール", "gender": 0, "channel_id": "UCUc8GZfFxtmk7ZwSO7ccQ0g"}
    TOKO_INUI = {"name": "戌亥とこ", "gender": 0, "channel_id": "UCXRlIK3Cw_TJIQC5kSJJQMg"}
    KAEDE_HIGUCHI = {"name": "樋口楓", "gender": 0, "channel_id": "UCsg-YqdqQ-KFF0LNk23BY4A"}
    RENA_YORUMI = {"name": "夜見れな", "gender": 0, "channel_id": "UCL34fAoFim9oHLbVzMKFavQ"}
    IBRAHIM = {"name": "イブラヒム", "gender": 1, "channel_id": "UCmZ1Rbthn-6Jm_qOGjYsh5A"}
    KEISUKE_MAIMOTO = {"name": "舞元啓介", "gender": 1, "channel_id": "UCJubINhCcFXlsBwnHp0wl_g"}
    RIN_SHIZUKA = {"name": "静凛", "gender": 0, "channel_id": "UC6oDys1BGgBsIC3WhG1BovQ"}
    AKINA_SAEGUSA = {"name": "三枝明那", "gender": 1, "channel_id": "UCNW1Ex0r6HsWRD4LCtPwvoQ"}
    DEVI_DEVI_DEVIL = {"name": "でびでび・でびる", "gender": 2, "channel_id": "UCjlmCrq4TP1I4xguOtJ-31w"}
    RATNA_PETIT = {"name": "ラトナ・プティ", "gender": 0, "channel_id": "UCIG9rDtgR45VCZmYnd-4DUw"}
    KAKERU_YUMEOI = {"name": "夢追翔", "gender": 1, "channel_id": "UCTIE7LM5X15NVugV7Krp9Hw"}
    BELLEMONDE_BANDERAS = {"name": "ベルモンド・バンデラス", "gender": 1, "channel_id": "UCbc8fwhdUNlqi-J99ISYu4A"}
    SISTER_CLAIRE = {"name": "シスター・クレア", "gender": 0, "channel_id": "UC1zFJrfEKvCixhsjNSb1toQ"}
    CHAIKA_HANABATAKE = {"name": "花畑チャイカ", "gender": 2, "channel_id": "UCsFn_ueskBkMCEyzCEqAOvg"}
    MIREI_GUNDO = {"name": "郡道美鈴", "gender": 0, "channel_id": "UCeShTCVgZyq2lsBW9QwIJcw"}
    FUYUKI_HAKASE = {"name": "葉加瀬冬樹", "gender": 0, "channel_id": "UCGYAYLDE7TZiiC8U6teciDQ"}
    KANA_SUKOYA = {"name": "健屋花那", "gender": 0, "channel_id": "UC8C1LLhBhf_E2IBPLSDJXlQ"}
    RIKIICHI_JOE = {"name": "ジョー・力一", "gender": 1, "channel_id": "UChUJbHiTVeGrSkTdBzVfNCQ"}
    KAZAKI_MORINAKA = {"name": "森中花咲", "gender": 0, "channel_id": "UCtpB6Bvhs1Um93ziEDACQ8g"}
    FUREN_E_LUSTARIO = {"name": "フレン・E・ルスタリオ", "gender": 0, "channel_id": "UCuep1JCrMvSxOGgGhBfJuYw"}
    GWELU_OS_GAR = {"name": "グウェル・オス・ガール", "gender": 1, "channel_id": "UC1QgXt46-GEvtNjEC1paHnw"}
    CHIMA_MACHITA = {"name": "町田ちま", "gender": 0, "channel_id": "UCo7TRj3cS-f_1D9ZDmuTsjw"}
    ROA_YUZUKI = {"name": "夢月ロア", "gender": 0, "channel_id": "UCCVwhI5trmaSxfcze_Ovzfw"}
    MIKOTO_RINDOU = {"name": "竜胆尊", "gender": 0, "channel_id": "UCPvGypSgfDkVe7JG2KygK7A"}
    KOKORO_AMAMIYA = {"name": "天宮こころ", "gender": 0, "channel_id": "UCkIimWZ9gBJRamKF0rmPU8w"}
    TOMOE_SHIRAYUKI = {"name": "白雪巴", "gender": 0, "channel_id": "UCuvk5PilcvDECU7dDZhQiEw"}
    HARU_KAIDA = {"name": "甲斐田晴", "gender": 1, "channel_id": "UCo2N7C-Z91waaR6lF3LL_jw"}
    ELU = {"name": "エルフのエル", "gender": 0, "channel_id": "UCYKP16oMX9KKPbrNgo_Kgag"}
    TAMAKI_FUMINO = {"name": "文野環", "gender": 0, "channel_id": "UCBiqkFJljoxAj10SoP2w2Cg"}
    LEVI_ELIPHA = {"name": "レヴィ・エリファ", "gender": 0, "channel_id": "UCtnO2N4kPTXmyvedjGWdx3Q"}
    DOLA = {"name": "ドーラ", "gender": 0, "channel_id": "UC53UDnhAAYwvNO7j_2Ju1cQ"}
    KOU_UZUKI = {"name": "卯月コウ", "gender": 1, "channel_id": "UC3lNFeJiTq6L3UWoz4g1e-A"}
    MASHIRO = {"name": "ましろ", "gender": 0, "channel_id": "UCfki3lMEF6SGBFiFfo9kvUA"}
    MAKAINO_RIRIMU = {"name": "魔界のリリム", "gender": 0, "channel_id": "UC9EjSJ8pvxtvPdxLOElv73w"}
    SHELLIN_BURGUNDY = {"name": "シェリン・バーガンディ", "gender": 1, "channel_id": "UCHBhnG2G-qN0JrrWmMO2FTA"}
    SHOICHI_KANDA = {"name": "神田笑一", "gender": 1, "channel_id": "UCWz0CSYCxf4MhRKPDm220AQ"}
    MARIN_HAYAMA = {"name": "葉山まりん", "gender": 0, "channel_id": "UCfipDDn7wY-C-SoUChgxCQQ"}
    RITSUKI_SAKURA = {"name": "桜凛月", "gender": 0, "channel_id": "UCfQVs_KuXeNAlGa3fb8rlnQ"}
    ALISE_MONONOBE = {"name": "物述有栖", "gender": 0, "channel_id": "UCt0clH12Xk1-Ej5PXKGfdPA"}
    MEIJI_WARABEDA = {"name": "童田明治", "gender": 0, "channel_id": "UCveZ9Ic1VtcXbsyaBgxPMvg"}
    RIRI_YUHI = {"name": "夕陽リリ", "gender": 0, "channel_id": "UC48jH1ul-6HOrcSSfoR02fQ"}
    HAJIME_SHIBUYA = {"name": "渋谷ハジメ", "gender": 1, "channel_id": "UCeK9HFcRZoTrvqcUCtccMoQ"}
    CHIGUSA_NISHIZONO = {"name": "西園チグサ", "gender": 0, "channel_id": "UCkngxfPbmGyGl_RIq4FA3MQ"}
    KEI_NAGAO = {"name": "長尾景", "gender": 1, "channel_id": "UCXW4MqCQn-jCaxlX-nn-BYg"}
    MASARU_SUZUKI = {"name": "鈴木勝", "gender": 1, "channel_id": "UCryOPk2GZ1meIDt53tL30Tw"}
    TOJIRO_GENZUKI = {"name": "弦月藤士郎", "gender": 1, "channel_id": "UCGw7lrT-rVZCWHfdG9Frcgg"}
    FUMI = {"name": "フミ", "gender": 0, "channel_id": "UCwrjITPwG4q71HzihV2C7Nw"}
    MAO_MATSUKAI = {"name": "魔使マオ", "gender": 0, "channel_id": "UCerkculBD7YLc_vOGrF7tKg"}
    NARAKA = {"name": "奈羅花", "gender": 0, "channel_id": "UC-o-E6I3IC2q8sAoAuM6Umg"}
    SOU_HAYASE = {"name": "早瀬走", "gender": 0, "channel_id": "UC2OacIzd2UxGHRGhdHl1Rhw"}
    UIHA_AIBA = {"name": "相羽ういは", "gender": 0, "channel_id": "UCnRQYHTnRLSF0cLJwMnedCg"}
    SAYO_AMEMORI = {"name": "雨森小夜", "gender": 0, "channel_id": "UCRWOdwLRsenx2jLaiCAIU4A"}
    LUIS_CAMMY = {"name": "ルイス・キャミー", "gender": 0, "channel_id": "UCb6ObE-XGCctO3WrjRZC-cw"}
    HARUKA_ONOMACHI = {"name": "小野町春香", "gender": 0, "channel_id": "UCg63a3lk6PNeWhVvMRM_mrQ"}
    SHIBA_KUROI = {"name": "黒井しば", "gender": 2, "channel_id": "UCmeyo5pRj_6PXG-CsGUuWWg"}
    HISUI_KITAKOJI = {"name": "北小路ヒスイ", "gender": 0, "channel_id": "UCRqBKoKuX30ruKAq05pCeRQ"}
    ICHIGO_USHIMI = {"name": "宇志海いちご", "gender": 0, "channel_id": "UCmUjjW5zF1MMOhYUwwwQv9Q"}
    GAKU_FUSHIMI = {"name": "伏見ガク", "gender": 1, "channel_id": "UCXU7YYxy_iQd3ulXyO-zC2w"}
    KARUTA_YAMAGAMI = {"name": "山神カルタ", "gender": 0, "channel_id": "UCllKI7VjyANuS1RXatizfLQ"}
    EMA_AUGUST = {"name": "えま・おうがすと", "gender": 0, "channel_id": "UCl1oLKcAq93p-pwKfDGhiYQ"}
    ELI_CONiFER = {"name": "エリー・コニファー", "gender": 0, "channel_id": "UCpNH2Zk2gw3JBjWAKSyZcQQ"}
    MANAMI_AIZONO = {"name": "愛園愛美", "gender": 0, "channel_id": "UC0WwEfE-jOM2rzjpdfhTzZA"}
    SETO_MIYAKO = {"name": "瀬戸美夜子", "gender": 0, "channel_id": "UCHK5wkevfaGrPr7j3g56Jmw"}
    MOIRA = {"name": "モイラ", "gender": 0, "channel_id": "UCvmppcdYf4HOv-tFQhHHJMA"}
    MAHIRO_YUKISHIRO = {"name": "雪城眞尋", "gender": 0, "channel_id": "UCHX7YpFG8rVwhsHCx34xt7w"}
    YOKO_AKABANE = {"name": "赤羽葉子", "gender": 0, "channel_id": "UCBi8YaVyZpiKWN3_Z0dCTfQ"}
    AKANE_ASAHINA = {"name": "朝日南アカネ", "gender": 0, "channel_id": "UCe_p3YEuYJb8Np0Ip9dk-FQ"}
    KYOKO_TODOROKI = {"name": "轟京子", "gender": 0, "channel_id": "UCRV9d6YCYIMUszK-83TwxVA"}
    NATSUME_KURUSU = {"name": "来栖夏芽", "gender": 0, "channel_id": "UCRcLAVTbmx2-iNcXSsupdNA"}
    NARU_NARUSE = {"name": "成瀬鳴", "gender": 1, "channel_id": "UCoM_XmK45j504hfUWvN06Qg"}
    SANGO_SUO = {"name": "周央サンゴ", "gender": 0, "channel_id": "UCL_O_HXgLJx3Auteer0n0pA"}
    HINA_ASUKA = {"name": "飛鳥ひな", "gender": 0, "channel_id": "UCiSRx1a2k-0tOg-fs6gAolQ"}
    MUGI_IENAGA = {"name": "家永むぎ", "gender": 0, "channel_id": "UC_GCs6GARLxEHxy1w40d6VQ"}
    KIRAME_SORAHOSHI = {"name": "空星きらめ", "gender": 0, "channel_id": "UC_82HBGtvwN1hcGeOGHzUBQ"}
    AKI_SUZUYA = {"name": "鈴谷アキ", "gender": 1, "channel_id": "UCpnvhOIJ6BN-vPkYU9ls-Eg"}
    MOMO_AZUCHI = {"name": "安土桃", "gender": 0, "channel_id": "UC6TfqY40Xt1Y0J-N18c85qQ"}
    AIR_HARUSAKI = {"name": "春崎エアル", "gender": 1, "channel_id": "UCtAvQ5U0aXyKwm2i4GqFgJg"}
    GILZAREN_THIRD = {"name": "ギルザレンⅢ世", "gender": 1, "channel_id": "UCUzJ90o1EjqUbk2pBAy0_aw"}
    RINE_YAGURUMA = {"name": "矢車りね", "gender": 0, "channel_id": "UCvzVB-EYuHFXHZrObB8a_Og"}
    TSUMUGU_KATARIBE = {"name": "語部紡", "gender": 0, "channel_id": "UCufQu4q65z63IgE4cfKs1BQ"}
    LIZE_HELESTA = {"name": "リゼ・ヘルエスタ", "gender": 0, "channel_id": "UCZ1xuCK1kNmn5RzPYIZop3w"}
    ANGE_KATRINA = {"name": "アンジュ・カトリーナ", "gender": 0, "channel_id": "UCHVXbQzkl3rDfsXWo8xi2qw"}
