# doc-writer v3 来源

给维护者看，skill 运行时不读。只收 research/VERIFY.md 核对过、或调研里标明已打开原文的来源。
标「建议」的条目在调研中属于推论或综合，skill 里只写成建议。设计稿和用户需求基线直接决定的条目（六阶段编排、MoSCoW、每节句长 60 字、处理表 20 行）不另列来源。

## SKILL.md、references/orchestration.md
- 依据设计稿 v3-spec.md 与任务卡「用户已定」；无外部来源。

## references/review.md
- 该不该现在决定：
  - Nygard ADR：https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
  - arc42 §9：https://docs.arc42.org/section-9/
  - Bezos 2015 致股东信：https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
  - Bezos 2016 致股东信：https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders
  - Fowler《Is Design Dead?》：https://martinfowler.com/articles/designDead.html
  - Fowler YAGNI：https://martinfowler.com/bliki/Yagni.html
  - Shape Up 第 2、5、6 章：https://basecamp.com/shapeup/1.1-chapter-02 、https://basecamp.com/shapeup/1.4-chapter-05 、https://basecamp.com/shapeup/1.5-chapter-06
  - Atwood, The Last Responsible Moment：https://blog.codinghorror.com/the-last-responsible-moment/
- 写多重与非目标：Design Docs at Google https://www.industrialempathy.com/posts/design-docs-at-google/ ；SRE Book, Embracing Risk https://sre.google/sre-book/embracing-risk/ 。「写成结论或删除」与待问标准属综合（建议）。
- 图和表：Google 开发者文档风格指南 Images https://developers.google.com/style/images ；Google 技术写作 Visual cues https://developers.google.com/tech-writing/accessibility/self-study/visual-cues ；Mermaid 状态图 https://mermaid.js.org/syntax/stateDiagram.html 与时序图 https://mermaid.js.org/syntax/sequenceDiagram.html 。状态数约 7、参与者不超过 5、一图一问属推论（建议），参考 Cowan 2001 https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf 。
- 段落与句子：阮一峰《中文技术文档的写作规范》https://raw.githubusercontent.com/ruanyf/document-style-guide/master/docs/paragraph.md 、https://raw.githubusercontent.com/ruanyf/document-style-guide/master/docs/text.md 。

## references/writing/product.md
- Atlassian PRD 指南：https://www.atlassian.com/agile/product-management/requirements
- Atlassian 验收标准：https://www.atlassian.com/work-management/project-management/acceptance-criteria
- Kevin Yien PRD 模板：https://docs.google.com/document/d/1mEMDcHmtQ6twzNlpvF-9maNlAcezpWDtCnyIqWkODZs/edit
- Lenny 1-pager：https://docs.google.com/document/d/1541V32QgSwyCFWxtiMIThn-6n-2s7fVWztEWVa970uo/edit
- Cucumber Better Gherkin：https://cucumber.io/docs/bdd/better-gherkin/
- Mountain Goat 用户故事：https://www.mountaingoatsoftware.com/agile/user-stories
- Working Backwards PR/FAQ：https://www.workingbackwards.com/concepts/working-backwards-pr-faq-process/
- 需求质量特征（单一、无歧义、可验证）经论文转述 ISO/IEC/IEEE 29148，未见标准正文：https://arxiv.org/html/2408.10886v1

## references/writing/tech.md
- Design Docs at Google：https://www.industrialempathy.com/posts/design-docs-at-google/
- Rust RFC 模板：https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md
- PEP 1：https://peps.python.org/pep-0001/
- arc42：https://docs.arc42.org/home/
- Nygard ADR：https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Oxide RFD 1：https://rfd.shared.oxide.computer/rfd/0001

## references/writing/reference.md
- Diátaxis Reference：https://diataxis.fr/reference/
- OpenAPI 规范：https://spec.openapis.org/oas/latest.html
- Google API 参考注释：https://developers.google.com/style/api-reference-comments
- Google 代码文本：https://developers.google.com/style/code-in-text
- Google 语态：https://developers.google.com/style/voice
- Google Highlights（条件放在指令前）：https://developers.google.com/style/highlights

## references/writing/ops.md
- SRE Workbook On-Call：https://sre.google/workbook/on-call/
- SRE Workbook Postmortem Culture：https://sre.google/workbook/postmortem-culture/
- SRE Book Postmortem Culture：https://sre.google/sre-book/postmortem-culture/
- PagerDuty 复盘模板：https://response.pagerduty.com/after/post_mortem_template/
- PagerDuty During an Incident：https://response.pagerduty.com/during/during_an_incident/
- Google 步骤写法：https://developers.google.com/style/procedures

## references/writing/test.md
- ISTQB CTFL Syllabus v4.0.1（§1.3、§4.2、§4.5.2、§5.1、§5.3、§5.5）：https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
- Cucumber Better Gherkin：https://cucumber.io/docs/bdd/better-gherkin/
- Fowler TestCoverage：https://martinfowler.com/bliki/TestCoverage.html
- Software Engineering at Google 第 11 章：https://abseil.io/resources/swe-book/html/ch11.html

## references/writing/marketing.md
- April Dunford：https://www.aprildunford.com/
- Amazon Working Backwards：https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
- GitHub Docs, About READMEs：https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- Mailchimp Style Guide：https://styleguide.mailchimp.com/tldr/ 、https://styleguide.mailchimp.com/voice-and-tone/
- NN/g：https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/ 、https://www.nngroup.com/articles/comparison-tables/
- Google Timeless documentation：https://developers.google.com/style/timeless-documentation
- Keep a Changelog 1.1.0：https://keepachangelog.com/en/1.1.0/

## references/unslop.md
- unslop（Lauren Tan，backnotprop/pstack，MIT 许可），本地副本 research/ext/unslop-SKILL.md。中文条目为改写，未复制原文。

## references/constraints-writing.md、scripts/doc-lint.py
- 原样沿用 v2 版 skill。G4 改编自阮一峰《中文技术文档的写作规范》（公共领域）。
