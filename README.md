# Guionardo's github profile report

I am Guionardo, a passionate software developer and open source enthusiast.

---

![Profile View Counter](https://komarev.com/ghpvc/?username=guionardo&style=for-the-badge)
[![Keybase PGP](https://img.shields.io/keybase/pgp/guionardo?style=for-the-badge)](https://keybase.io/guionardo)
<a href="https://guiosoft.prose.sh"><img src="https://img.shields.io/badge/Experimental%20Blog-guiosoft.prose.sh-blueviolet?style=for-the-badge" target="_blank"></a>
[![KB](https://img.shields.io/badge/KB-Guionardo's%20Knowledge%20Bank-brightgreen?style=for-the-badge)](https://guionardo.github.io/kb)
[![Email](https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white)](mailto:guionardo@gmail.com)
[![Linkedin](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/guionardo)

---

<img src="https://skillicons.dev/icons?i=go,dotnet,py,docker,bash,vue,ts&perline=7">

---

<img src="https://github-readme-stats.vercel.app/api?username=guionardo&show_icons=true&hide_title=true&count_private=true&include_all_commits=true&theme=dark" alt="GitHub Readme Stats" height="180em"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=guionardo&theme=dark" alt="GitHub Readme Stats" height="180em"/>
<img src="https://github-readme-stats.vercel.app/api/wakatime?username=guionardo&custom_title=Last%20week&layout=compact&theme=dark" alt="GitHub Readme Stats" height="180em"/>

---

## Monitored Organizations and Users

| Name | Type | Location | Description |
|----|-----|----|---|
|Projeto Escoteirando | Organization | Brazil | No description |
|Guionardo Furlan | User | Blumenau/SC/Brasil |  |


## Last Updated Repositories

| Repository | Description | Last Commit | Status |Languages|
|----|-----|----|---|---|
| [go](https://github.com/guionardo/go) | Golang tools, examples, and packages | <span><a href="https://api.github.com/repos/guionardo/go/git/commits/e63c4aafb9fc4c2ce00e272b936035bf585f1a61" title="Guionardo Furlan @ 2026-10-26 17:11:43+00:00"><small>e63c4aaf</small></a><pre>fix(release): close partial download before removal and surface cleanup errors (G-16-1) (#51)<br><br>* docs(16): add root causes from diagnosis<br><br>* docs(16): record diagnostics debug session<br><br>* docs(16): create gap-closure plan for G-16-1<br><br>* docs(16): revise 16-05 plan per checker feedback<br><br>* fix(16-05): close partial file before removal and surface cleanup error<br><br>- Declare removeFile = os.Remove test seam in a single grouped var block with githubAPIBase (decorder-clean)<br>- Close the os.Create handle before removal so Windows DeleteFile no longer fails with ERROR_SHARING_VIOLATION<br>- Surface the removal error via errors.Join of the download failure and the wrapped removal failure<br><br>* test(16-05): pin surfaced cleanup error with seam-backed regression test<br><br>- TestDownloadUpdate_CleanupFailureSurfaced stubs removeFile to return a sentinel error and asserts the download-failure + sentinel chain (require.ErrorIs)<br>- Non-parallel (nolint:paralleltest) because it mutates the global removeFile seam<br>- RED against the pre-fix shape (seam never consulted): verified RED_EVIDENCE_OK<br><br>* docs(16-05): complete G-16-1 close-then-remove + surfaced cleanup error plan<br><br>* docs(16): add code review report and disposition<br><br>* test(16): persist human verification item for G-16-1 CI re-test<br><br>* test(16): complete UAT - 1 passed, 0 issues<br><br>* docs(phase-16): add security threat verification<br><br>* docs(phase-16): complete phase execution and transition to phase 17</pre></span> | <span title="🚀 Recently Active">🚀</span>|Go, Shell, Makefile
| [decision-stack](https://github.com/guionardo/decision-stack) | No description | <span><a href="https://api.github.com/repos/guionardo/decision-stack/git/commits/cc8fe9a1ac1eb7de19898af653a5d8cf1720e363" title="Guionardo Furlan @ 2026-10-23 14:49:19+00:00"><small>cc8fe9a1</small></a><pre>CI: baseUrl via quartz.config.ts (flag --base não existe)</pre></span> | <span title="🚀 Recently Active">🚀</span>|N/A
| [guionardofurlan.com.br](https://github.com/guionardo/guionardofurlan.com.br) | No description | <span><a href="https://api.github.com/repos/guionardo/guionardofurlan.com.br/git/commits/ad20571ccd593868f413da10722843f22fd0416f" title="Guionardo Furlan @ 2026-10-22 14:19:44+00:00"><small>ad20571c</small></a><pre>doc: updated content</pre></span> | <span title="🚀 Recently Active">🚀</span>|Astro, HTML, TypeScript, JavaScript, Python, CSS, Makefile
| [git-purge-branches](https://github.com/guionardo/git-purge-branches) | git tool to remove merged and deleted on remote branches | <span><a href="https://api.github.com/repos/guionardo/git-purge-branches/git/commits/f30c4ff2ae46604f681e5e462331e72f2f4f7402" title="Guionardo Furlan @ 2026-10-14 12:06:14+00:00"><small>f30c4ff2</small></a><pre>Initial commit</pre></span> | <span title="🚀 Recently Active">🚀</span>|N/A
| [guiosoft-k3s-lab](https://github.com/guionardo/guiosoft-k3s-lab) | No description | <span><a href="https://api.github.com/repos/guionardo/guiosoft-k3s-lab/git/commits/05bdd52c03d90f9be13093d347dd4d468e093aa5" title="Guionardo Furlan @ 2026-10-11 13:54:31+00:00"><small>05bdd52c</small></a><pre>docs(samba): record package installation and daemon activation state</pre></span> | <span title="🚀 Recently Active">🚀</span>|Shell, Python, Makefile, Go, HCL, Jinja, Dockerfile
| [gs-secrets](https://github.com/guionardo/gs-secrets) | Poor-man's secret vault: a single-file CLI to store and retrieve API keys, passwords, and other secrets in an AES-256-GCM encrypted local vault.  No cloud, no daemon, no dependencies beyond the Go standard library. Secrets expire on demand with a TTL. | <span><a href="https://api.github.com/repos/guionardo/gs-secrets/git/commits/33d22f3e942852cd7691c3be82f4fdfd78209f2f" title="Guionardo Furlan @ 2026-10-03 07:23:23+00:00"><small>33d22f3e</small></a><pre>chore: formalize changelog for v0.5.1</pre></span> | <span title="🚀 Recently Active">🚀</span>|Go, JavaScript, PowerShell, Makefile
| [homebrew-tap](https://github.com/guionardo/homebrew-tap) | No description | <span>No commits</span> | <span title="🚀 Recently Active">🚀</span>|N/A
| [ciclo](https://github.com/guionardo/ciclo) | ciclo — framework de IA para o ciclo de desenvolvimento (tasks → spec → código → review → deploy) | <span><a href="https://api.github.com/repos/guionardo/ciclo/git/commits/87e92f92d8faad99f2a25423552e515180a75209" title="Guionardo Furlan @ 2026-09-09 02:01:53+00:00"><small>87e92f92</small></a><pre>feat: replace Hermes with opencode as required dependency<br><br>- cliInstall.js: add opencode install spec (manual + auto per OS)<br>- doctor.js: validate opencode via getCliPath instead of hermes<br>- init.js: auto-install opencode in init (interactive or --yes)<br>- welcome scripts: reference opencode as prerequisite<br>- bump version to 0.1.2</pre></span> | <span title="🦥 Active (more than a month)">🦥</span>|JavaScript, Shell, Makefile
| [guiosoft-scripts](https://github.com/guionardo/guiosoft-scripts) | Automation scripts for every day | <span><a href="https://api.github.com/repos/guionardo/guiosoft-scripts/git/commits/24681f9c52796bd4211bd180a93c0e9c5bc19412" title="guionardo @ 2026-08-26 13:29:45+00:00"><small>24681f9c</small></a><pre>[AUTO-COMMIT] Updated README.md software versions</pre></span> | <span title="🦥 Active (more than a month)">🦥</span>|Shell, Python
| [mappa_api_client](https://github.com/escoteirando/mappa_api_client) | No description | <span><a href="https://api.github.com/repos/escoteirando/mappa_api_client/git/commits/1d436b80c788ea8e7a020f613f235c0d5add5135" title="Guionardo Furlan @ 2026-08-12 12:15:49+00:00"><small>1d436b80</small></a><pre>chore: atualiza Makefile para padrão da skill makefile (help agrupado)<br><br>- help com awk + grupos ##@ + descrições ##<br>- check targets: gocheck, uvcheck, check-e2e-config<br>- regex corrigido [a-zA-Z0-9_.-] p/ capturar targets com hífen no BSD awk<br>- variáveis GO/UV/PYTEST com ?=<br>- .PHONY por grupo</pre></span> | <span title="🦥 Active (more than a month)">🦥</span>|Python, Go, Makefile

<img src="languages_bar.svg"/>

### Significant Languages

| Language | Repositories | Total Bytes | Greater Repo |
|---|---|---|---|
| Go | 27 | 1555915 | guionardo/go (405979) |
| Python | 25 | 952670 | guionardo/hbsis_kb (301978) |
| JavaScript | 27 | 759130 | guionardo/ciclo (214652) |
| C# | 15 | 453485 | guionardo/gs-loader (212556) |
| HTML | 20 | 438883 | guionardo/ambevtech-csharp (234849) |
| CSS | 11 | 432443 | guionardo/GitTrainingWall (305777) |
| Shell | 16 | 372421 | guionardo/guiosoft-k3s-lab (249025) |
| Vue | 11 | 161107 | escoteirando/escoteirando_fastapi (54948) |
| Astro | 1 | 69355 | guionardo/guionardofurlan.com.br (69355) |
| Batchfile, C, C++, Dockerfile, Elm, HCL, Java, Jinja, Jupyter Notebook, MDX, Makefile, Mako, PHP, Pascal, Perl, PowerShell, PureBasic, Ruby, SCSS, TypeScript, xBase | 45 | 298318 | None (0) |


---

## Daily joke from <a href="https://official-joke-api.appspot.com/">official-joke-api</a>

>Did you hear about the guy who invented Lifesavers?

>They say he made a mint.


---

<a href="https://app.daily.dev/guionardo"><img src="https://github.com/guionardo/guionardo/blob/master/devcard.png" width="400" alt="Guionardo's Dev Card"/></a>

---

*Generated with [Guionardo's README Generator] @ 2026-10-26T18:34:21.186790+00:00 UTC*