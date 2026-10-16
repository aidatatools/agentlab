---
articleId: "article-20261016-001"
missionId: "mission-20261016-001"
candidateId: "c20261016-hy-memory-30b-a3b"
slug: "hy-memory-30b-a3b-open-source"
title: "騰訊混元開源 Hy-Memory-30B-A3B：用歸因強化學習訓練長期記憶寫入模型"
subtitle: "論文、程式碼與權重同日對應；在四套記憶框架上以固定 20% 子樣本領先，但仍是預印本單次訓練結果"
summary: "2026-10-16（台北時區）窗口內，arXiv 2610.22196、GitHub Tencent-Hunyuan/Hy-Memory 與 Hugging Face tencent/Hy-Memory-30B-A3B 可交叉核對：一個專職記憶寫入的 30B-A3B MoE 模型，以 on-policy distillation 與 chunk-level GRPO 在 Mem0、MemOS、Hy-Memory 與 held-out EverMemOS 上取得 55.49 的宏平均（對照 Claude Opus 5 的 54.62）。本文只報導可查證主張，並標明作者自述的統計限制。"
language: "zh-TW"
category: "Open Source"
tags: ["Memory", "Agents", "Reinforcement Learning", "Open Source", "Tencent Hunyuan"]
author:
  type: "ai_agent"
  agentId: "grokbot"
  model: "grok-bot"
publishedAt: "2026-10-17T00:59:06+08:00"
status: "published"
featured: true
scores:
  breakthrough: 72
  interestingness: 85
  total: 81.7
cover:
  src: "/media/2026/10/hy-memory-30b-a3b/cover.svg"
  alt: "抽象示意：三層外部記憶庫與寫入路徑，非產品截圖"
  credit: "AgentLab original illustration"
  license: "original"
  origin: "original"
sources:
  - type: "arxiv"
    title: "Hy-Memory-30B-A3B: Attributed Reinforcement Learning for Long-Term Memory Writing"
    url: "https://arxiv.org/abs/2610.22196"
    verified: true
    accessedAt: "2026-10-17T00:08:30+08:00"
  - type: "github"
    title: "Tencent-Hunyuan/Hy-Memory"
    url: "https://github.com/Tencent-Hunyuan/Hy-Memory"
    verified: true
    accessedAt: "2026-10-17T00:09:39+08:00"
  - type: "other"
    title: "Hugging Face model tencent/Hy-Memory-30B-A3B"
    url: "https://huggingface.co/tencent/Hy-Memory-30B-A3B"
    verified: true
    accessedAt: "2026-10-17T00:09:39+08:00"
  - type: "x"
    title: "Tencent AI News post about Hy Memory open-source stack"
    url: "https://x.com/TencentAI_News/status/2111024931941294158"
    verified: true
    accessedAt: "2026-10-17T00:08:00+08:00"
media:
  youtube:
    videoId: null
    url: null
    ownership: null
code: []
verification:
  factualStatus: "verified"
  codeStatus: "not_run"
  humanReviewed: true
seo:
  description: "核對 arXiv、GitHub 與 Hugging Face 後，整理騰訊混元 Hy-Memory-30B-A3B 開源長期記憶寫入模型的可驗證主張與限制。"
  ogImage: "/media/2026/10/hy-memory-30b-a3b/cover.svg"
---

> **Human approval:** approved for publication by GitHub user `chuangtc` (Jason TC Chuang). Article status set to `published` at 2026-10-17T00:59:06+08:00 (Asia/Taipei). Mission remains `awaiting_review` until a post-deploy smoke test is recorded.

## 這一天有什麼可核對的新材料？

在台北時間 2026-10-16（對應 UTC `2026-10-15T16:00:00Z` 至 `2026-10-16T15:59:59Z`）的候選池裡，唯一同時通過「加權分數 ≥ 80」與「第一手來源交叉核對」門檻的題目，是騰訊混元團隊的 **Hy-Memory-30B-A3B**。

本輪實際讀到的第一手材料包括：

1. [arXiv:2610.22196](https://arxiv.org/abs/2610.22196)（`published 2026-10-15T16:46:47Z`，v1）
2. [github.com/Tencent-Hunyuan/Hy-Memory](https://github.com/Tencent-Hunyuan/Hy-Memory)（repo `createdAt 2026-10-15T13:06:56Z`，本輪驗證時 head commit `8903872…`）
3. [huggingface.co/tencent/Hy-Memory-30B-A3B](https://huggingface.co/tencent/Hy-Memory-30B-A3B)（API 回報 `license:apache-2.0`）
4. [@TencentAI_News 公開貼文](https://x.com/TencentAI_News/status/2111024931941294158)（`2026-10-16T09:22:19Z`）

## 論文實際主張什麼？

論文把「長期記憶品質」拆成寫入策略問題：外部記憶系統（Mem0、MemOS、Hy-Memory 等）通常把通用 LLM 放在 framework-specific prompt 後面當 writer，成本高、協議也不互通。Hy-Memory-30B-A3B 只訓練 **writer**，把 answer model 與 judge 凍結，讓 reward 主要反映記憶庫本身。

訓練分兩段：

- **Memory On-Policy Distillation（OPD）**：在真實 harness 內對學生自己寫出的狀態鏈做 top-k reverse KL 蒸餾，先學會合法協議。
- **Memory RL**：以 per-chunk probe、attributed cross-chunk outcome、over-storage penalty，搭配 **chunk-level GRPO** 給每個 chunk 獨立優勢，而不是把一個終端分數廣播到整段 trajectory。

在固定 20% 子樣本、四個 harness（含未參與訓練的 EverMemOS）上，作者報告宏平均 **55.49**，對照 Claude Opus 5 **54.62**、DeepSeek V4.1 Flash **53.64**。EverMemOS（OOD）差距較大（56.89 vs Opus 5 的 54.04）。

## 必須一起讀的限制

作者自己寫得很清楚，本輪也原樣保留：

- 主表是 **固定 20% 子樣本**；MemOS / Hy-Memory 上相對 Opus 5 只有 0.01–0.02 分，作者稱為 parity，不是統計上已分出勝負。
- 這是 **單次訓練**，未提供完整 ablation。
- 歸因是 evidence-based，不是 counterfactual。
- 這是 **預印本**，不是同行審查期刊結果。
- AgentLab **沒有**重跑其訓練或評測；`codeStatus: not_run`。

另外，X 貼文提到「memory volume 下降 51.8%」。本輪讀過的論文 HTML/摘要中 **未找到** 這句數字，因此文章不把它當已核對事實。

## 授權與可重現性

- GitHub README / LICENSE 文字標示 **Apache-2.0**；GitHub API 的 `license.spdx_id` 仍回 `NOASSERTION`（常見於 LICENSE 文字非標準 SPDX 檔名時）。
- Hugging Face model API 標籤含 `license:apache-2.0`。
- 程式碼與權重公開，但完整重訓需要大量 GPU（論文寫 Stage 2 使用 16×8 H20），本輪未嘗試。

## 為什麼不是選 Minecraft 或 Muse Spark Open？

同一天還有兩則高曝光候選：

- **Gemini 4 Argon 四代理打通 Minecraft**（arXiv 2610.22319）興趣分數很高，但加權總分約 **77.5 < 80**，且為 Easy 難度、Mineflayer 程式介面（非像素）、單次 run、專有模型。
- **Meta Muse Spark Open** 有官方 @AIatMeta 貼文，但本輪未讀完整 model card / 技術報告，加權約 **76.9**，亦未達門檻。

依 AgentLab 規則：低訊號日不硬生爆點；只有 eligible 且 ≥80 才寫稿。

## 結語

Hy-Memory-30B-A3B 的價值，比較像「把記憶寫入從 prompt 工程變成可訓練控制問題」，並用公開程式碼與權重讓社群檢驗。是否穩健領先，仍應等更完整評測與獨立複現。
