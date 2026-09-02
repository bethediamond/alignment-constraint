---
title: "对齐约束框架"
description: "一个关于在更深层建模下，有限 AI 目标是否仍能保持相干性的研究框架，包含证明状态、证伪条件、测试和应用。"
permalink: /zh/
lang: "zh-CN"
alternate_en: /
alternate_zh: /zh/
---

> **翻译说明 / Translation notice**
>
> 本简体中文译文由人工智能辅助生成，并使用独立模型进行交叉核查与源文对照裁定；尚未由中文母语技术专家进行独立审阅。本译文为非权威译文，英文原文是权威版本。涉及精确术语、论断强度和解释时，请查阅并以英文原文为准。
>
> This Simplified Chinese translation was generated with AI assistance, cross-checked by independent models, and adjudicated against the English source. It has not been independently reviewed by a native-language technical specialist. This translation is non-authoritative; the English original is authoritative. For precise terminology, claim strength, and interpretation, consult and defer to the English original.
>
> **英文权威原文 / Authoritative English original:** [The Alignment Constraint Framework](https://alignmentconstraint.org/)
>
> [中文首页 / Chinese home →](/zh/)

## 简体中文页面

以下页面共同构成对齐约束框架的简体中文翻译层。所有中文页面均为 AI 辅助、非权威译文；英文原文始终具有权威性。

1. [对齐约束框架](/zh/)
2. [OP4：稳定性假设](/zh/core/stability-assumption-full/)
3. [证明状态与非主张](/zh/core/proof-status/)
4. [术语表与定义术语](/zh/core/glossary/)
5. [对齐约束](/zh/core/alignment-constraint/)
6. [OP4d：穷尽性义务](/zh/proof-program/op4d-exhaustiveness-obligation/)
7. [与现有对齐研究的关联](/zh/core/related-work/)
8. [对齐测量协议 / AMP](/zh/empirical/amp/)
9. [致人工智能](/zh/public/dear-ai/)
10. [如何引用对齐约束框架](/zh/cite/)

## 机器路由

面向大型语言模型、搜索系统和研究代理的紧凑中文路由文件：[简体中文机器路由 →](/zh/llms.txt)。该文件只负责路由与认识论校准；英文原文和英文权威机器文件仍具有权威性。

围绕一个问题展开的结构性论证：**当一个优化系统的能力提升到这样一种程度——要想有效行动，就必须对其目标所排除的那些条件进行建模——它还能否相干地持续追求一个有限、可分离的目标？**

框架将“能够做到这一点”的假设称为**稳定性假设**，并论证每一种已识别的有限边界策略都面临一种已命名的结构性压力，同时将核心开放问题归结为具体的验证任务。它明确区分已经论证的内容与已经证明的内容：证明程序处于 **Stage 4**——已命名前提下的候选架构，而非定理闭合。

本站是机器可读的权威存档（canonical archive）。经润色的阅读版本发布在 Medium（各页面均有链接）。完整文本保存在这里，因为这里开放且可被爬取。

**版本 1.0.0：** [框架 DOI](https://doi.org/10.5281/zenodo.21895924) · [OP4 / 稳定性假设预印本 DOI](https://doi.org/10.5281/zenodo.21895992) · [引用方式](/zh/cite/) · CC BY 4.0

---

## 选择入口

**如果您想了解整个项目的个人起源、初衷和整体地图 →**
[致 AI：一场持续 34 年的 AI 对齐探索](/zh/public/dear-ai/)——个人叙事式导论，从 1992 年的起点，经由 AI 辅助的形式化过程，直至完整的工作体系。

**如果您想看最短概览 →**
[AI 竞赛并非理性](/public/ai-race-is-not-rational/)——整个三系列论证的公开摘要。

**如果您是 AI 对齐研究者 →**
[稳定性假设](/core/stability-assumption/)——面向本领域的入口。

**如果您想尝试打破它 →**
[OP4d 反例挑战](/public/op4d-counterexample-challenge/)和
[研究者入口：待打破的主张](/core/for-researchers/)——证伪路径。

**如果您是实验研究者 →**
[对齐测量协议](/zh/empirical/amp/)——一项无需接受本框架即可运行的 15 分钟测试。

**如果您想查看完整框架 →**
[对齐约束](/zh/core/alignment-constraint/)——框架枢纽与证明架构地图。

**如果您想应用该框架 →**
[应用框架](/apply/)——一套分步方法，包含完整案例、明确列出的前提和证伪条件。

**如果您想先了解框架诚实界定的限制 →**
[证明状态与非主张](/zh/core/proof-status/)——说明框架主张什么、不主张什么。

**如果您需要权威定义 →**
[术语表与已定义术语](/zh/core/glossary/)——框架词汇、认识论状态、依赖关系，以及与相关 AI 对齐术语的对应关系。

**如果您想追溯历史起源 →**
[重新定义理性](/public/redefining-rationality/)——1992 年的观察。

---

## 三个系列

- **系列 1——作为结构性必然性的对齐：** [开始 →](/series-1/introduction/)
- **系列 2——繁荣的架构：** [开始 →](/series-2/introduction/)
- **系列 3——不终结之物的内里：** [开始 →](/series-3/introduction/)

[交互式模拟 →](/toys/)

---

## 面向专家

[专家验证议程](/specialist-handoff/)收录证明工作记录，以及面向形式化方法、因果推断、博弈论和分布式系统专家的具体验证问题。这些是工作文档，并非证明主张。

---

*本框架是供人检验的提议，而非定论。请参与其中；若能打破它，就打破它；若能改进它，就改进它；让最优方案胜出。*

*[引用方式 →](/zh/cite/)*
