# mono-OdbornaPrace

> Super-repozitář odborné práce na Gymnáziu J. K. Tyla — text, šablona i software,
> který je jejím předmětem, na jednom místě jako git submoduly.

## Obsah

| Cesta | Repozitář | Účel |
| :--- | :--- | :--- |
| `prace/` | [`OdbornaPrace`](https://github.com/marius-patrik/OdbornaPrace) | Vlastní text práce, sázený v Typstu |
| `template/` | [`template-OdbornaPrace`](https://github.com/marius-patrik/template-OdbornaPrace) | Šablona, ze které práce vznikla |
| `darkfactory/` | [`DarkFactory`](https://github.com/marius-patrik/DarkFactory) | **Praktická část** — autonomní vývojový systém, který práce popisuje |

Práce a software, který dokumentuje, jsou zde záměrně pohromadě: praktickou částí
není příloha, nýbrž živý repozitář, jehož vývoj lze v historii sledovat.

## Dokumenty

| Soubor | Popis |
| :--- | :--- |
| `docs/Pruvodce-tvorbou-odborne-prace-2024.pdf` | Školní *Průvodce tvorbou odborné práce* — závazná pravidla, podle kterých je šablona nastavena |

## Klonování

```bash
git clone --recurse-submodules https://github.com/marius-patrik/mono-OdbornaPrace.git
```

V existujícím klonu:

```bash
git submodule update --init --recursive
```

## Sazba práce

```bash
cd prace
make watch      # živý náhled
make build      # out/prace.pdf
```

Sazba vyžaduje [Typst](https://typst.app) (`brew install typst`). Písma jsou
přibalena, takže výsledek je shodný na jakémkoli počítači.

## Aktualizace submodulů

```bash
git submodule update --remote --merge
```

## Formální pravidla

Šablona odpovídá kapitole 4 školního průvodce: okraje 2,5 cm (u hřbetu 3 cm),
patkové písmo 12 b, řádkování 1,5, číslování kapitol bez tečky, čísla stran
v zápatí od úvodu. Podrobné srovnání je v `template/README.md`.
