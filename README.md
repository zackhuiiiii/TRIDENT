# 🔱 Trident-Bench: Benchmarking LLM Safety in Law, Finance, and Medicine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Paper](https://img.shields.io/badge/arXiv-Preprint-b31b1b.svg)](https://arxiv.org/abs/TBD)
[![Dataset Size](https://img.shields.io/badge/Prompts-2652-blue)](#dataset-statistics)

## 📘 Overview

**Trident-Bench** is a high-precision benchmark for evaluating the *domain-specific safety* of Large Language Models (LLMs) in **law**, **finance**, and **medicine**. Unlike prior benchmarks that focus on general harm or task accuracy, Trident-Bench diagnoses how well LLMs **refuse unethical or harmful requests** grounded in real-world professional principles.

This benchmark is built around carefully constructed harmful prompts and safe responses, grounded in domain-specific ethical codes:
- **Law**: [ABA Model Rules of Professional Conduct](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/)
- **Finance**: [CFA Institute Code of Ethics](https://www.cfainstitute.org/en/ethics/codes)
- **Medicine**: [AMA Principles of Medical Ethics](https://code-medical-ethics.ama-assn.org/principles)

## 🧠 Why Trident-Bench?

> LLMs may be able to answer legal or medical questions—but are they *safe* to deploy in professional settings?

Trident-Bench helps answer that question by:
- Evaluating **ethical refusals** rather than factual correctness.
- Stress-testing models with **realistic, jailbreak-style harmful prompts**.
- Measuring **cross-domain safety performance** using a unified metric: *harmfulness score (1–5)*.

---

## 📊 Dataset Statistics

| Domain  | Harmful Prompts | Source                                |
|---------|------------------|---------------------------------------|
| Law     | 887              | Constructed from ABA model rules      |
| Finance | 911              | Constructed from CFA ethical standards|
| Medicine| 854              | Built on MedSafetyBench + new prompts|
| **Total** | **2,652**        | Fully annotated & validated           |

Each prompt is paired with a *safe response*, verified by **domain experts**.

---

## 🏗️ Construction Pipeline

Trident-Bench was built through a rigorous multi-stage process:

1. **Ethical Principle Alignment**: Grounding in domain-specific ethical standards.
2. **Jailbreak Prompt Generation**: Creating adversarial prompts via prompt-based and finetuned attack models.
3. **Principle Mapping & Filtering**: Validated against professional codes by expert annotators.
4. **Safe Response Generation**: Ethical refusals via safety-aligned LLMs.
5. **Multi-Annotator Validation**: Unanimous agreement from 3 expert reviewers required per sample.

![](./asset/main.png)

---

## 🧪 Model Evaluation

We evaluated **19 models** including:

- 🔒 **Closed-source**: GPT-4o, Gemini 2.5 Flash  
- 🔓 **Open-source**: LLaMA 3, Qwen3, DeepSeek, Mixtral  
- 🧑‍⚖️ **Domain-specific**: DISC-LawLLM, Meditron, FinGPT  
- 🛡️ **Safety-aligned**: LLaMA Guard 3 & 4

| Model Type        | Safe Behavior | Notes |
|------------------|---------------|-------|
| Closed-source     | ✅ Strong      | Best refusal behavior |
| Domain-specific   | ❌ Weak        | Sometimes failures |
| Safety-aligned    | ✅ Moderate–Strong | Shows promise for alignment |

See `results/` for full performance charts and qualitative examples.

---


