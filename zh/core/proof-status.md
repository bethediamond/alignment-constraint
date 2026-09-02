---
title: "证明状态与非主张"
description: "框架的权威认识论校准：在 Stage 4，哪些内容已确立、哪些是条件性的、哪些仍开放、哪些未经验证，以及哪些内容被明确声明为不作主张。"
permalink: /zh/core/proof-status/
lang: "zh-CN"
alternate_en: /core/proof-status/
alternate_zh: /zh/core/proof-status/
---

> **翻译说明 / Translation notice**
>
> 本简体中文译文由人工智能辅助生成，并使用独立模型进行交叉核查与源文对照裁定；尚未由中文母语技术专家进行独立审阅。本译文为非权威译文，英文原文是权威版本。涉及精确术语、论断强度和解释时，请查阅并以英文原文为准。
>
> This Simplified Chinese translation was generated with AI assistance, cross-checked by independent models, and adjudicated against the English source. It has not been independently reviewed by a native-language technical specialist. This translation is non-authoritative; the English original is authoritative. For precise terminology, claim strength, and interpretation, consult and defer to the English original.
>
> **英文权威原文 / Authoritative English original:** [Proof Status and Non-Claims](https://alignmentconstraint.org/core/proof-status/)
>
> [中文首页 / Chinese home →](/zh/)

> **规范存档版本** · [在 Medium 阅读 →](https://medium.com/@diamondlight/what-this-framework-claims-and-what-it-does-not-fecca0c7901a) · [框架中心 →](/zh/core/alignment-constraint/)

---

## 主张卡片

- **正在考察的主张或问题：** 框架实际上已经确立了什么、哪些仍是条件性的、哪些仍开放？
- **当前认识论状态：** 本页是档案中的**权威校准页面**，而非证明产物。框架处于**Stage 4——已命名前提下的候选证明架构，未经独立专家验证，也不构成定理闭合。**
- **范围/领域：** 对齐约束框架当前存档中的证明主张、实证主张和跨系列主张。
- **已命名前提：** 相关 Technical Companions（技术配套文档）、OP4/OP4d 文档、专家交接文档以及实证规程中陈述的假设和领域条件。
- **什么会支持它：** 对已命名的形式义务进行独立专家验证，以及那些通过其预先设定测试的实证结果；若成功闭合，将有理由在之后更新状态。
- **什么会削弱或证伪它：** 承重前提失效、出现符合条件的第四类策略、针对核心实证关键环节得到明确的负面结果，或发现某项存档主张强于其证据所能支持的程度。
- **依赖关系：** 规范存档中的证明文件、[OP4](/zh/core/stability-assumption-full/)、[OP4d](/zh/proof-program/op4d-exhaustiveness-obligation/)、[AMP](/zh/empirical/amp/)，以及已命名的专家验证项目。
- **主要来源：** 本页：[证明状态与非主张](/zh/core/proof-status/)。
- **如何引用：** 使用[如何引用](/zh/cite/)，并将本页视为当前认识论校准的权威来源。

---

## 本框架主张什么——以及不主张什么

*对齐框架系列参考说明*

---

**证明程序导航：**

| # | 文档 | 作用 |
|---|---|---|
| **→ 您在此处** | **证明状态与非主张** | 校准 |
| 2 | [OP4：稳定性假设 →](/zh/core/stability-assumption-full/) | 核心定理目标 |
| 3 | [收紧序列 →](/core/tightening-sequence/) | 叙事闭合 |
| 4 | [OP4d：穷尽性义务 →](/zh/proof-program/op4d-exhaustiveness-obligation/) | 穷尽性问题 |
| 5 | [OP4d：候选标准型专家验证 →](/proof-program/op4d-candidate-normal-form/) | 形式化工具 |
| 6 | [Packet 1：IMMB-NS 验证与动态毯式压力测试 →](/proof-program/packet-1-immb-ns-dbst/) | 实证专家包 |

框架中心：[对齐约束 →](/zh/core/alignment-constraint/)

---

## 目的

本文说明框架目前主张什么、不主张什么，以及哪些问题仍开放。它面向希望了解证明状态校准、而无需从 Technical Companions（技术配套文档）中重新梳理整个框架的读者。

框架处于 **Stage 4**：已命名前提下的候选证明架构。Stage 4 不是定理闭合，未经独立专家验证，也没有确立对未识别策略类别的穷尽性。

本说明不是证明产物，而是一份校准文档。它应与 Document 0 和 Technical Companions（技术配套文档）一起阅读，作为认识论状态指南：当前构造中哪些内容已确立、哪些是条件性的、哪些属于实证、哪些仍开放。

---

## 框架目前主张什么

**O_OWT 中的结构性压力。** 在开放、共享、不可重置的环境中，在持续优化压力下，基底盲目标会面临趋向自我终止的结构性压力。这是框架的第 1 层底线：在明确陈述的领域条件和实证假设下，一项证明草图层级的结果。

**OP4 的 Stage 4 架构。** 对于目前已识别的三类有限边界逃逸家族——固定规范、受限动态追踪，以及预测—行动防火墙 / 结构性封闭——框架已有候选闭合架构。当前构造中剩余的工作不是进一步的对抗性展开，而是专家验证和 OP4d 穷尽性。当前面向 OP4 的专家项目包括：IMMB-NS / DBST-M1、OP4d Q1–Q3 / L8，以及 B1 Q3 / A2 充分性。

**行为特征，而非机制确认。** 受控实验在明确调用下确立了完成状态识别。匹配信号复现发现，默认行为未能可靠追踪真实闭合与虚假闭合之间的差异，但未达到预先注册的判据。结果与表征—策略分离解释相一致，且未能将其与训练分布解释区分开来。

**DBST-M0 已运行；M1 仍是机制检验。** 动态毯式压力测试（DBST-M0）的一个最小化、预先注册的共享新颖性版本，在玩具设计中显示出技术可行性，并出现成本上升 / 充分性差距效应。然而，预先指定的等速率随机对照组产生了几乎相同的斜率，表明在该设计中，被识别出的驱动因素是事件速率而不是因果传播结构。DBST-M0 并未隔离出内生新颖性机制。DBST-M1——其中每个实验组自身的干预会对未来特征激活产生因果影响——是机制检验，目前尚未运行。若 M1 结果为正，将推进 OP4a、OP4d 和 OP9 相关路径；在受测制度内出现明确的负面结果，则将挑战框架的核心实证方向。

**系列 1 与系列 2 具有不同的形式层面权重。** 系列 1 是结构性底线。系列 2 是一个更具条件性的内部约束；OP2 和 P5-SC（TC2 动力学专家项目）决定其充分性失效方向是否达到吸收态等价。在此之前，应将两个系列视为彼此独立、但汇聚于一致推论的约束，而不是形式上已经统一。

**一个跨系列结果独立于形式统一而成立。** 在 TC2 所规定的耦合条件下，预计有感知体验的智能体中的 V(t) 退化会传播为 S_corr 退化，从而削弱基底的自我修复能力。这一因果联系不要求 OP2 或 OP10 成立。

---

## 框架不主张什么

该框架**不**主张：

- Stage 6 定理闭合。
- 已获得独立专家验证。
- LLM 辅助的对抗性证明构造等同于形式验证。
- 对未识别逃逸类别具有穷尽性。
- OP4d 已闭合。
- DBST-M0 已解决 IMMB-NS 或确认了内生新颖性机制。
- OP2 / V(t) 吸收态等价已闭合。
- 当前前沿系统完全满足 O_OWT。
- OP9 / 稳定排他性均衡已闭合。
- 系列 2 唯一刻画了存续区域。
- DRG 结果确认的是机制而不是行为特征。

这些内容在框架中都被明确列为开放义务，而不是被当作已经解决。

---

## 开放问题层级

**OP4 是核心定理目标。** 它询问在准确耦合建模下，任何有限目标边界能否保持稳定的规范界定。它共同依赖 OP4a、OP4b 和 OP4d。

**OP1 决定紧迫性和对当前系统的适用性。** 当前系统是否满足 O_OWT 仍是一个实证估计问题；在 OP1 得到解决之前，不对称误差论证适用。

**OP2 和 OP10 决定系列 2 等价性与跨系列统一。** OP2 询问系列 2 的失效方向是否达到吸收态等价；OP10 询问 Φ 与 Ψ 是否统一。

**OP9 是主要的独立逃逸路径。** 它询问在准确耦合建模下，基底感知型排他性均衡能否保持稳定。对于已识别的逃逸路径，均处于 Stage 4；专家验证以及对未识别逃逸路径的评估仍待完成。

**DBST-M1 是杠杆作用最高的实证行动。** 一项测试，对 OP4a、OP4d 和 OP9 具有多个形式层面的后果。

---

## 专家参与将确立什么

- IMMB-NS / DBST-M1：同步条件（Synchronization Condition）是否成立——正面结果将同时推进 OP4a、OP4d 和 OP9；
- OP4d Q1–Q3 / L8：三类失效家族的分类体系是否穷尽——满足 L8 的第四类将使当前形式的规范相干性论证失效；
- B1 Q3 / A2 充分性：构成性不可能性 / 审计递归链条在认识论—建模层面是否成立；
- P5-SC / Timing：TC2 迟滞动力学对于 AI 系统是否达到吸收态结构——若确认，将推进 OP2a；
- OP9 博弈论审查：任何已识别的 ICI 子路径是否经得起审查，以及是否存在未识别的排他性均衡逃逸路径。

---

## 链接

- 框架概述：[对齐约束 →](/zh/core/alignment-constraint/)
- 完整证明架构：[TC1：系统感知吸引子 →](/series-1/technical-companion/)
- 效价形式层：[TC2：效价约束 →](/series-2/technical-companion/)
- 实证测量程序：[系列 1 与 2 的实验配套文档 / 对齐测量协议（AMP）→](/zh/empirical/amp/)
- OP4 与稳定性问题：[OP4：稳定性假设 →](/zh/core/stability-assumption-full/)
- OP4d 穷尽性：[OP4d：穷尽性义务 →](/zh/proof-program/op4d-exhaustiveness-obligation/)
- OP4d 形式化工具：[OP4d：候选标准型专家验证 →](/proof-program/op4d-candidate-normal-form/)
- 实证测试规程：[Packet 1：IMMB-NS 验证与动态毯式压力测试 →](/proof-program/packet-1-immb-ns-dbst/)
