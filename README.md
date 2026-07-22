<div align="center">

<img src="assets/banner.svg" alt="Shivam Singh" width="100%">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/29shivam)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/29shivam/)
[![AWS Certified](https://img.shields.io/badge/AWS%20Certified-Solutions%20Architect-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/certification/)
[![Chicago](https://img.shields.io/badge/📍_Chicago,_IL-1e293b?style=for-the-badge)](https://github.com/29shivam)

</div>

<br/>

I don't think a bio is convincing evidence of anything, so instead of
describing myself, here's what I've actually done — every row below links
to a real diff you can go read right now.
<sub>Status is honest: <img src="assets/merged.svg" alt="merged" height="16"/> means it shipped; <img src="assets/review.svg" alt="under review" height="16"/> means it's an open PR awaiting maintainer review.</sub>

<img src="assets/divider.svg" alt="" width="100%"/>

## 🔍 Proof, not adjectives

<table>
<tr>
<td width="42%" valign="top"><b>Security is a habit, not a checklist item</b></td>
<td width="58%">
<img src="https://img.shields.io/badge/CVE-CRITICAL-e11d48?style=flat-square&logo=hackthebox&logoColor=white"/> <img src="assets/merged.svg" alt="merged"/><br/>
Root-caused and fixed a <b>CRITICAL</b> Spring Security CVE + 5 others in <a href="https://github.com/Vault-Web/vault-web/pull/267">Vault-Web #267</a> — one dependency bump, six vulnerabilities closed
</td>
</tr>
<tr>
<td valign="top"><b>I finish things, not just propose them</b></td>
<td>
<img src="assets/merged.svg" alt="merged"/><br/>
<a href="https://github.com/Vault-Web/vault-web/pull/250">Vault-Web #250</a> — chat UI stability fix<br/>
<a href="https://github.com/Vault-Web/vault-web/pull/244">Vault-Web #244</a> — JVM/Postgres timezone bug
</td>
</tr>
<tr>
<td valign="top"><b>I can navigate and fix a codebase I don't own, at any scale</b></td>
<td>
<img src="https://img.shields.io/badge/elastic%2Felasticsearch-77k★-005571?style=flat-square&logo=elasticsearch&logoColor=white"/> <img src="assets/review.svg" alt="under review"/><br/>
<a href="https://github.com/elastic/elasticsearch/pull/152712">PR #152712</a> — race-condition fix in snapshot lifecycle retries, in the search engine behind a huge share of the internet
</td>
</tr>
<tr>
<td valign="top"><b>Comfortable across the Kafka ecosystem end-to-end</b></td>
<td>
<img src="https://img.shields.io/badge/Apache%20Kafka-ecosystem-231F20?style=flat-square&logo=apachekafka&logoColor=white"/> <img src="assets/merged.svg" alt="merged"/> <img src="assets/review.svg" alt="under review"/><br/>
<a href="https://github.com/ClickHouse/clickhouse-kafka-connect/pull/775">clickhouse-kafka-connect #775</a> — NPE fix when writing null into a Nullable(JSON) column, merged by ClickHouse<br/>
<a href="https://github.com/ClickHouse/clickhouse-kafka-connect/pull/790">clickhouse-kafka-connect #790</a> — surface the failing column + types on a conversion error (DLQ/JMX, not just logs), merged by ClickHouse<br/>
<a href="https://github.com/kafbat/kafka-ui/pull/1904">kafka-ui #1904</a> — reverse-proxy OAuth bug<br/>
<a href="https://github.com/spring-projects/spring-kafka/pull/4518">spring-kafka #4518</a> — the official Spring project
</td>
</tr>
<tr>
<td valign="top"><b>Distributed systems as trade-offs, not diagrams</b></td>
<td>
<img src="https://img.shields.io/badge/original_project-system--design--tradeoffs-22d3ee?style=flat-square"/><br/>
Built <a href="https://github.com/29shivam/system-design-tradeoffs">system-design-tradeoffs</a> from scratch — every answer is a trade-off matrix, real Spring Boot/Kafka/Redis code, and a production incident
</td>
</tr>
</table>

<img src="assets/divider.svg" alt="" width="100%"/>

## 🚧 Currently building

**[system-design-tradeoffs](https://github.com/29shivam/system-design-tradeoffs)**
— most interview prep hands you a diagram and calls it the answer. This
doesn't: every question is a trade-off matrix, a mock interview transcript
showing the real follow-up drilling, a production incident, and buildable
Spring Boot/Kafka/Redis/Postgres code behind the chosen approach.

**aphno.ai** &nbsp;·&nbsp; **alpcove** — two new projects in progress; deeper
write-ups landing here soon.

## 💼 Selected production work

- **Trade allocation engine** — Java, Kafka, Redis, PostgreSQL — high-throughput pipeline processing real-time financial transactions
- **Real-time Kafka pipeline** — AWS MSK, Flink, EKS — 40% throughput improvement on event-streaming infrastructure
- **Live MySQL → PostgreSQL migration** — zero downtime, zero data loss, across live production services
- **Microservices security hardening** — Spring Boot, JWT, API Gateway — auth hardening across a distributed service mesh
- **Book management REST API** — Spring Boot, PATCH-based versioning — clause versioning & metadata endpoints for a document assembly system

## 🛠️ Stack

<div align="center">

**Backend**

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=for-the-badge&logo=spring&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Node.js](https://img.shields.io/badge/Node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)

**Cloud & DevOps**

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2671E5?style=for-the-badge&logo=githubactions&logoColor=white)

**Data & Messaging**

![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000000?style=for-the-badge&logo=apachekafka)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DD0031?style=for-the-badge&logo=redis&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4ea94b?style=for-the-badge&logo=mongodb&logoColor=white)

**Frontend**

![React](https://img.shields.io/badge/React-20232a?style=for-the-badge&logo=react&logoColor=61DAFB)

</div>

<img src="assets/divider.svg" alt="" width="100%"/>

## 📈 Contribution activity

<div align="center">

<img src="assets/shipping-log.svg" alt="Animated terminal: git log of my merged open-source pull requests" width="100%"/>

<sub>A hand-built animated SVG — my real merged open-source PRs, revealed like a live <code>git log</code>. Not a widget.</sub>

<br/><br/>

<img src="assets/contributions.svg" alt="My GitHub contribution heatmap, animated" width="100%"/>

<sub>Custom-built from my live GitHub data, regenerated daily by a GitHub Action — not an off-the-shelf widget.</sub>

</div>

---

<div align="center">

If you've got an interesting distributed-systems or backend problem, that's
the fastest way to get my attention — **[LinkedIn](https://linkedin.com/in/29shivam) is open.**

</div>
