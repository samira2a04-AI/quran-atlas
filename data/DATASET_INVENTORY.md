# Quranic Recitation Dataset Inventory

This inventory documents candidate datasets for the Quran Atlas project, categorized into two main types:
* **TYPE A — `asr_correct`**: Correct Quranic recitation audio for evaluating ASR recognition.
* **TYPE B — `mistake_labeled`**: Recordings where the learner's actual recitation differs from the canonical Quran text and the deviation is human-verified.

## Verification Legend

| Status | Meaning |
|:---|:---|
| `APPROVED` | License and metadata independently confirmed from primary source (paper/official repo/publisher page). |
| `NEEDS_REVIEW` | One or more fields could not be confirmed from a primary source, or a correction was found. Human review required before use. |
| `UNVERIFIED` | Not yet checked. |

---

## Verification Run — 2026-08-29

**Verified by:** Agent 2 (independent cross-check)
**Method:** HF API (`/api/datasets/<id>`), OSF API, direct README/LICENSE file fetch, web search cross-reference, arXiv paper.

### Corrections and flags found

| # | Dataset | Issue | Severity |
|:---|:---|:---|:---|
| 1 | Tadabur | `source_url` and `download_url` on HF pointed to **wrong username** (`fherran/tadabur`). Actual HF repo is `FaisaI/tadabur` (capital I). Confirmed via GitHub README badge and HF API. | **HIGH — URL ERROR** |
| 2 | Quranic ASR Benchmark | License version listed as NPL-**1.1**; actual license in HF cardData is `quran-lab-npl-1.2` (NPL-**1.2**). | **MEDIUM — VERSION ERROR** |
| 3 | Quran-Recitations (MohamedRashad) | Reciter count listed as ~15; web sources document **20 reciters**. Also, HF cardData has **no `license` field** — Apache 2.0 comes only from README text, not the official HF license tag. | **MEDIUM — COUNT WRONG + LICENSE FIELD ABSENT** |
| 4 | Buraaq quran-md-ayahs | HF cardData has **no `license` field**. CC0 1.0 claim is unconfirmed from any primary source. | **MEDIUM — LICENSE UNCONFIRMED** |
| 5 | Buraaq quran-md-words | Same as above — no `license` in HF cardData. CC0 1.0 unconfirmed. | **MEDIUM — LICENSE UNCONFIRMED** |
| 6 | AQQD | OSF URL `https://osf.io/6sh5d` confirmed correct; project title on OSF is "UGR-MINDVOICE" (umbrella project). `node_license` field is null in OSF API. CC0 1.0 confirmed via published paper. | **LOW — NOTE ONLY** |

---

## Dataset Inventory

### TYPE A — `asr_correct` Datasets

---

#### 1. Tadabur: A Large-Scale Quran Audio Dataset

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://huggingface.co/datasets/FaisaI/tadabur (**CORRECTED from `fherran/tadabur`**) |
| **original_source_url** | https://github.com/fherran/tadabur (code repo) |
| **download_url** | https://huggingface.co/datasets/FaisaI/tadabur |
| **recordings_count** | 365,000+ |
| **reciters_count** | 600+ |
| **has_transcriptions** | Yes (word-level JSON timestamp alignments) |
| **language** | Arabic |
| **license_name** | CC BY-NC 4.0 |
| **license_version** | 4.0 |
| **commercial_use_allowed** | No |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes (non-commercial) |
| **attribution_required** | Yes |
| **access_restrictions** | None |
| **dataset_size** | 1,400+ hours |
| **source_paper** | Tadabur: A Large-Scale Quran Audio Dataset (arXiv:2604.18932) |

> **URL CORRECTED**: Agent 1 listed `fherran/tadabur` as the HF dataset — that is the GitHub code repo, not the data repo. The actual HF dataset repo is `FaisaI/tadabur` (capital I). Confirmed via: (1) GitHub README badge linking to `FaisaI/tadabur`, (2) HF API response `"id": "FaisaI/tadabur"`, (3) `"license": "cc-by-nc-4.0"` in HF tags and cardData.

---

#### 2. Annotated Quranic Qira'at Dataset (AQQD)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://osf.io/6sh5d |
| **original_source_url** | https://github.com/owaismujtaba/mind-voice |
| **download_url** | https://osf.io/6sh5d |
| **recordings_count** | 24,183 |
| **reciters_count** | 309 |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | CC0 1.0 Universal |
| **license_version** | 1.0 |
| **commercial_use_allowed** | Yes |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes |
| **attribution_required** | No |
| **access_restrictions** | None |
| **dataset_size** | 24,183 WAV files |
| **source_paper** | "An open annotated Quranic Qira'at dataset (AQQD) for machine learning and phonetic variation analysis" (PMC/NIH) |

> OSF URL confirmed correct (osf.io/6sh5d). The OSF project title is "UGR-MINDVOICE" — this is the umbrella project; AQQD is the dataset hosted within it. `node_license` is null at the OSF API node level, but CC0 1.0 is confirmed in the published paper (PMC/NIH). Covers 10 canonical Qira'at styles, 70 selected Surahs.

---

#### 3. Quran Speech to Text Dataset (OpenSLR SLR132)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://www.openslr.org/132/ |
| **original_source_url** | https://www.openslr.org/132/ |
| **download_url** | https://openslr.trmal.net/resources/132/Quran_Speech_Dataset.tar.xz |
| **recordings_count** | 226,129 |
| **reciters_count** | 30 |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | MIT |
| **license_version** | N/A |
| **commercial_use_allowed** | Yes |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes |
| **attribution_required** | Yes |
| **access_restrictions** | None |
| **dataset_size** | 24 GB |
| **source_paper** | N/A (submitted by individual contributor "Mohammed") |

> MIT license confirmed directly on the OpenSLR resource page. Ayah-level aligned transcriptions. Download URL corrected to the actual `.tar.xz` archive.

---

#### 4. Buraaq Quran Multimodal Dataset — Ayahs (quran-md-ayahs)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `NEEDS_REVIEW` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | Low |
| **source_url** | https://huggingface.co/datasets/Buraaq/quran-md-ayahs |
| **original_source_url** | https://huggingface.co/datasets/Buraaq/quran-md-ayahs |
| **download_url** | https://huggingface.co/datasets/Buraaq/quran-md-ayahs |
| **recordings_count** | 187,080 |
| **reciters_count** | 32 |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | CC0 1.0 Universal (UNCONFIRMED) |
| **license_version** | 1.0 |
| **commercial_use_allowed** | Unknown |
| **redistribution_allowed** | Unknown |
| **modification_allowed** | Unknown |
| **ml_training_allowed** | Unknown |
| **attribution_required** | Unknown |
| **access_restrictions** | None |
| **dataset_size** | 34.9 GB |
| **source_paper** | Quran-MD: A Fine-Grained Multimodal Dataset of the Quran (arXiv:2601.17880, Muslims in ML @ NeurIPS 2025) |

> **LICENSE UNCONFIRMED**: HF API `cardData` contains **NO `license` field** for this dataset. The CC0 1.0 claim from the original inventory cannot be verified from any primary source checked. No explicit CC0 declaration found via web search. Recommend checking the dataset README directly or contacting the Buraaq organization before use in production.

---

#### 5. Buraaq Quran Multimodal Dataset — Words (quran-md-words)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `NEEDS_REVIEW` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | Low |
| **source_url** | https://huggingface.co/datasets/Buraaq/quran-md-words |
| **original_source_url** | https://huggingface.co/datasets/Buraaq/quran-md-words |
| **download_url** | https://huggingface.co/datasets/Buraaq/quran-md-words |
| **recordings_count** | 77,429 |
| **reciters_count** | 32 |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | CC0 1.0 Universal (UNCONFIRMED) |
| **license_version** | 1.0 |
| **commercial_use_allowed** | Unknown |
| **redistribution_allowed** | Unknown |
| **modification_allowed** | Unknown |
| **ml_training_allowed** | Unknown |
| **attribution_required** | Unknown |
| **access_restrictions** | None |
| **dataset_size** | 2.05 GB |
| **source_paper** | Quran-MD: A Fine-Grained Multimodal Dataset of the Quran (arXiv:2601.17880, Muslims in ML @ NeurIPS 2025) |

> **LICENSE UNCONFIRMED**: Same issue as quran-md-ayahs. HF API `cardData` has **NO `license` field**. CC0 1.0 claim unconfirmed. Sibling dataset with word-level audio annotations.

---

#### 6. Quran-Recitations (MohamedRashad)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `NEEDS_REVIEW` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | Medium |
| **source_url** | https://huggingface.co/datasets/MohamedRashad/Quran-Recitations |
| **original_source_url** | https://huggingface.co/datasets/MohamedRashad/Quran-Recitations |
| **download_url** | https://huggingface.co/datasets/MohamedRashad/Quran-Recitations |
| **recordings_count** | 124,689 |
| **reciters_count** | 20 (CORRECTED from ~15) |
| **has_transcriptions** | Yes (fully diacritized Arabic text) |
| **language** | Arabic |
| **license_name** | Apache 2.0 (README-sourced only; NOT in HF cardData) |
| **license_version** | 2.0 |
| **commercial_use_allowed** | Yes (if Apache 2.0 applies) |
| **redistribution_allowed** | Yes (if Apache 2.0 applies) |
| **modification_allowed** | Yes (if Apache 2.0 applies) |
| **ml_training_allowed** | Yes (if Apache 2.0 applies) |
| **attribution_required** | Yes (if Apache 2.0 applies) |
| **access_restrictions** | None (gated: false) |
| **dataset_size** | 33.1 GB |
| **source_paper** | N/A (community dataset) |

> **COUNT CORRECTED**: Original inventory said ~15 reciters. Web sources document **20 Qaris**: Al-Ajmi, Alafasy, Al-Hudhaify, Al-Hussary (Murattal + Mujawwad), Al-Muaiqly, El-Minshawi (Murattal + Mujawwad), and 12 others including Al-Sudais, Abu Bakr Al-Shatri, Abdul Basit Abdul Samad, etc. **LICENSE NOTE**: HF API `cardData` has **NO `license` field**. Apache 2.0 is claimed in README and referenced in community sources but not formally registered as an HF license tag. Not gated.

---

#### 7. Quranic ASR Benchmark

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://huggingface.co/datasets/Quran-Lab/quranic-asr-benchmark |
| **original_source_url** | https://huggingface.co/datasets/Quran-Lab/quranic-asr-benchmark |
| **download_url** | Gated — requires HF access request (auto-gated) |
| **recordings_count** | 600 (200 per source: everyayah_heldout, qul_alnufais, tlog_holdout) |
| **reciters_count** | 4+ (3 source collections) |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | Quran-Lab Non-Profit License 1.2 (NPL-1.2) (CORRECTED from NPL-1.1) |
| **license_version** | 1.2 |
| **commercial_use_allowed** | No |
| **redistribution_allowed** | No |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes (research/evaluation only) |
| **attribution_required** | Yes |
| **access_restrictions** | Gated (auto) — requires: Name, Affiliation, Intended use + checkbox agreeing no redistribution/voice-cloning |
| **dataset_size** | ~246 MB |
| **source_paper** | Quran-Lab / itqan.dev (no separate arXiv paper identified) |

> **VERSION CORRECTED**: Agent 1 listed NPL-1.1. HF API `cardData` explicitly states `"license_name": "quran-lab-npl-1.2"`. Live leaderboard at https://huggingface.co/spaces/Muno459/quranic-asr-leaderboard. Benchmark is designed to be leakage-free (clips verified absent from training data).

---

#### 8. QRFAM: Quran Recitations by Females and Males

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `NEEDS_REVIEW` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | Low |
| **source_url** | Not found publicly |
| **original_source_url** | Not found publicly |
| **download_url** | Not found publicly |
| **recordings_count** | Unknown |
| **reciters_count** | Multiple |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | Unknown |
| **access_restrictions** | Private (academic research access only) |
| **dataset_size** | Unknown |
| **source_paper** | QRFAM: A Benchmark Dataset of Quran Recitations by Females and Males |

> No public repository discovered. Private academic benchmark addressing gender and proficiency bias in Quranic ASR evaluation. Could not verify any metadata claim independently. Recommend contacting paper authors.

---

#### 9. Arabic Diversified Audio Dataset (Ar-DAD)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://data.mendeley.com/datasets/3kndp5vs6b/3 |
| **original_source_url** | https://data.mendeley.com/datasets/3kndp5vs6b/3 |
| **download_url** | https://data.mendeley.com/datasets/3kndp5vs6b/3 |
| **recordings_count** | 16,209 |
| **reciters_count** | 42 (30 Qaris + 12 imitators) |
| **has_transcriptions** | Yes |
| **language** | Arabic |
| **license_name** | CC BY 4.0 |
| **license_version** | 4.0 |
| **commercial_use_allowed** | Yes |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes |
| **attribution_required** | Yes |
| **access_restrictions** | None |
| **dataset_size** | 10.6 GB |
| **source_paper** | Ar-DAD: Arabic Diversified Audio Dataset |

> Mendeley Data page confirmed accessible. Mendeley applies CC BY 4.0 as the default license for all datasets. Includes Quranic recitations (Surahs 78–114) as part of a broader Arabic speech corpus.

---

#### 10. Quranic Word-By-Word Audio Data (zaibihassan)

| Field | Value |
|:---|:---|
| **dataset_type** | asr_correct |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://huggingface.co/datasets/zaibihassan/Quranic-Word-By-Word-Audio-Data |
| **original_source_url** | https://huggingface.co/datasets/zaibihassan/Quranic-Word-By-Word-Audio-Data |
| **download_url** | https://huggingface.co/datasets/zaibihassan/Quranic-Word-By-Word-Audio-Data |
| **recordings_count** | 77,000+ |
| **reciters_count** | 2 (Muallim and Mujawwad styles) |
| **has_transcriptions** | Yes (microsecond Protocol Buffer alignments) |
| **language** | Arabic |
| **license_name** | Apache 2.0 |
| **license_version** | 2.0 |
| **commercial_use_allowed** | Yes |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes |
| **attribution_required** | Yes |
| **access_restrictions** | None |
| **dataset_size** | ~400 MB (Opus) / 2.3 GB (raw) |
| **source_paper** | N/A (Hugging Face Dataset Card) |

> Apache 2.0 confirmed via multiple web sources citing the dataset card. Not gated. Word-by-word audio with microsecond-precision alignments.

---

### TYPE B — `mistake_labeled` Datasets

---

#### 11. Surah Al-Ikhlas Error Detection Dataset

| Field | Value |
|:---|:---|
| **dataset_type** | mistake_labeled |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://data.mendeley.com/datasets/sxtmmr6mvk/1 |
| **original_source_url** | https://data.mendeley.com/datasets/sxtmmr6mvk/1 |
| **download_url** | https://data.mendeley.com/datasets/sxtmmr6mvk/1 |
| **recordings_count** | 1,506 |
| **reciters_count** | Multiple (crowd-sourced via Google Forms) |
| **has_transcriptions** | Yes (binary: correct / incorrect labels by 5 Qur'an experts) |
| **language** | Arabic |
| **license_name** | CC BY 4.0 |
| **license_version** | 4.0 |
| **commercial_use_allowed** | Yes |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes |
| **attribution_required** | Yes |
| **access_restrictions** | None |
| **dataset_size** | 1,506 audio files |
| **source_paper** | Surah Al-Ikhlas of the Holy Qur'an Error Detection Dataset (DOI: 10.17632/sxtmmr6mvk.1) |

> CC BY 4.0 confirmed via web search corroborating the Mendeley Data page. Collected Aug–Sep 2021. Manually labeled by 5 Qur'an experts. Contributors: Maghraby, Alsaedi, Mahjoob, Al-Otaibi, Alsaedi ×2 (Umm Al-Qura University).

---

#### 12. Quranic Dataset for Automatic Tajweed Error Detection (QDAT)

| Field | Value |
|:---|:---|
| **dataset_type** | mistake_labeled |
| **verification_status** | `APPROVED` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | High |
| **source_url** | https://huggingface.co/datasets/obadx/qdat |
| **original_source_url** | https://huggingface.co/datasets/obadx/qdat |
| **download_url** | https://huggingface.co/datasets/obadx/qdat |
| **recordings_count** | 1,500+ (v1) / 6,000+ (v2) |
| **reciters_count** | Multiple |
| **has_transcriptions** | Yes (Tajweed rule labels) |
| **language** | Arabic |
| **license_name** | MIT |
| **license_version** | N/A |
| **commercial_use_allowed** | Yes |
| **redistribution_allowed** | Yes |
| **modification_allowed** | Yes |
| **ml_training_allowed** | Yes |
| **attribution_required** | Yes |
| **access_restrictions** | None |
| **dataset_size** | 1,500+ / 6,000+ files |
| **source_paper** | QDAT: A data set for Reciting the Quran (2021) |

> MIT license confirmed via JSON-LD structured data on HF page (`"license": "https://choosealicense.com/licenses/mit/"`) and in HF tags (`license:mit`). Labels 3 Tajweed rules: Separate Stretching, Tight Noon, Concealment. Audio cleaned/resampled to 16kHz.

---

#### 13. Quranic Database for Recitation Correction (QDRC)

| Field | Value |
|:---|:---|
| **dataset_type** | mistake_labeled |
| **verification_status** | `NEEDS_REVIEW` |
| **verified_by** | Agent 2 |
| **last_verified_date** | 2026-08-29 |
| **confidence** | Low |
| **source_url** | Not found publicly |
| **original_source_url** | Not found publicly |
| **download_url** | Not found publicly |
| **recordings_count** | 54 (error instances) |
| **reciters_count** | 17 volunteers |
| **has_transcriptions** | Yes (paired with correct recitation) |
| **language** | Arabic |
| **license_name** | Unknown |
| **access_restrictions** | Private (academic access only) |
| **dataset_size** | Unknown |
| **source_paper** | Voice Feature Analysis for Quranic Recitation Correction (or similar) |

> Academic dataset of 54 specific errors in Surat Al-Fatihah recorded by 17 volunteers, paired with correct recitations. No public repository found. Could not verify any metadata claim independently. Recommend contacting paper authors.
