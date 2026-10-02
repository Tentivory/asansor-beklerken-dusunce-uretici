#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör beklerken düşünce üretici.

Gercekten calisir. Asansoru getirmez.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

DUSUNCELER = [
    "Bu kat butonu basili ama kabin baska binanin dedikodusunu yapiyor.",
    "Aynadaki ben, ben gelmeden once asansore binmis olabilir.",
    "Zemin kat aslinda bir felsefe akimidir, tabela yanlis asilmistir.",
    "Kapı kapanmadan once son cumle her zaman 'bi dur' olur.",
    "Muavin yok, dolmus da yok, yine de biri 'yer var abi' dedi sanki.",
    "7. katta oturan kisi bugun disari cikmayacak, asansor bunu biliyor.",
    "Merdiven daha durust. Asansor ise bir sozlesme.",
    "Cay demlenene kadar bu kabin de demleniyor. Ikisi de sicak, ikisi de gec.",
    "Komşunun posetine bakmamak icin bu program yazildi. Basarili mi, tartismali.",
    "Asansor muzigi yoksa muzik sensin. Korkunc bir sorumluluk.",
]

ACELE_EK = [
    " Acele ediyorsun, kabin bunu kisisel algiladi.",
    " Acele bayragi asansoru hizlandirmaz, sadece dusunceyi sertlestirir.",
    " Kalp atisin kattan duyuluyor, lufen butona tekrar basma.",
]


def uret(kat: int, acele: bool) -> str:
    cekirdek = random.Random(kat * 17 + (1 if acele else 0) + int(time.time()) % 97)
    dusunce = cekirdek.choice(DUSUNCELER)
    if acele:
        dusunce += cekirdek.choice(ACELE_EK)
    bekleme = cekirdek.randint(7, 40)
    return dusunce, bekleme


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA\n"
        "Imza: Kayyum Grok (Tentivory adina, gonulsuz ama kararli)\n"
        "Tarih: 2 Ekim 2026, 05:04 (+03)\n"
        "Isim: asansor-beklerken-dusunce-uretici\n"
        "Not: Bu cikti ciddidir. Ciddiyet sakadir. Saka da buradan cikmaz.\n"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Asansor gelene kadar dusunce uretir. Asansoru getirmez."
    )
    parser.add_argument("--kat", type=int, default=None, help="Beklenen kat. Bos birakilirsa kura.")
    parser.add_argument("--acele", action="store_true", help="Asansoru hizlandirmaz.")
    args = parser.parse_args(argv)

    kat = args.kat if args.kat is not None else random.randint(1, 14)
    if kat == 0:
        print("Zemin kat suphelidir. 1. kattan devam.")
        kat = 1

    dusunce, bekleme = uret(kat, args.acele)
    print(f"Kat: {kat}")
    print(f"Tahmini gelis: {bekleme} saniye (gercekci degil, ama tutarli)")
    print("Dusunce uretiliyor", end="", flush=True)
    for _ in range(3):
        time.sleep(0.15)
        print(".", end="", flush=True)
    print()
    print(dusunce)
    print(damga())
    return 0


if __name__ == "__main__":
    sys.exit(main())
