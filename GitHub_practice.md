# GitHub入门与协作
> 截至2026.3

## 1.1 新建GitHub仓库
1. 登录 `GitHub`
2. 右上角 ` + -> New repository `
3. 选择`owner`，个人或组织
4. 添加仓库名和描述（可选）
5. 选择可见性：` Public 或 Private `
6. 注：如果准备上传本地已有项目，建议不要勾选初始化`README/.gitgnore/License`（避免首次推从冲突）
7. 点击`Create repository`
## 1.2 配置 GitHub SSH
>目的:让`git clone/pull/push`免输账号密码，只需密钥验证
### 第一步： 生成SSH密钥
```bash
ssh-keygen -t -C "your_email"@example.com
```
默认生成：
- 私钥：` ~/.ssh/id_ed25519 `(严禁泄露)
- 公钥 `~/.ssh/id_ed25519.pub`(可上传`GitHub`)
###  第二步：启动ssh-agent并加载私钥
`Linux/macOS`:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519 
```
`Windows Poweshell`:
```bash
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
ssh-add $env:USERPROFILE\\.ssh\\id_ed25519
```
### 第三步：把公钥加到GitHub
1. 复制公钥内容
``` bash
cat ~/.ssh/id_ed_25519.pub
```
2. GitHub右上角头像 -> `settings` -> `SSH and GPG keys` -> `New SSH key`
3. `Title`填设备名（如`my-laptop`）,`key`粘贴公钥。
4. 点击 `Add SSH key`。
### 第四步：测试连接
```bash
ssh -T git@github.com
```
首次会提示主机指纹确认，输入yes
成功会看到类似：`Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.`
这是GitHub的安全政策，你的GitHub账号和本地SSH密钥已经成功绑定，可以安全进行`git clone`,`git push`,`git pull`
## 1.3 上传/下拉仓库（clone/pull/push）
### 1）下拉仓库(clone)
```bash
git clone git@github.com:YOUR_NAME/YOUR_REPO.git #本段在仓库出点击绿色的code，选择SSH获取
cd YOUR_REPO
```
### 2）拉取远端更新(pull)
```bash
git pull origin main
```
注：`origin`是远端默认名字， `main`是常见默认分支名        
### 3）上传本地提交(push)
```bash
git push origin main
```
### 首次把本地已有项目上传到新仓库
```bash
cd your_project
git init
git add.
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:TOUR_NAME/YOUR_REPO.git
git push -u origin main
```
`-u`作用：建立上游跟踪关系，后续可直接`git push / git pull`
## 1.4 如何提交更改(标准日常流程)
每次改代码后建议按这个顺序
```bash
git status  #查看仓库状态（哪些被修改、新增或删除，以及哪些在暂存区）
git add <files> # 将指定文件添加到暂存区，为提交做准备
git add . #添加当前目录及其子目录下所有有修改的文件 （与git add <files>类似），本步骤只标记
git commit -m "feat: add xxx" # 将暂存区的修改正式提交到本地git仓库，生成新的版本记录 
git push #将本地仓库的提交推送到远程仓库，使远程仓库与本地保持同步
```
注：`-m`后的提交描述(约定式提交的规范)
```
feat 新功能
fix 修复
docs 文档
refactor 重构
style 格式
test 测试
chore 构建/工具
（这些内容仅为提交描述，不会改变文件内容）
```
### 1.5 Issue是什么？如何创建？
`Issue`是什么

`Issue`是“任务/问题单”，用于跟踪`Bug`、需求、改进、讨论事项。

它不是代码本身，而是“要做什么”和“为什么做”的记录。

`Web`创建`Issue`
1. 进入仓库页面
2. 点击`Issue`标签
3. 点击 `New issue`
4. 选择模板（若有）或`Open a blank issue`。
5. 填写标题与描述，必要时加 `label`，`assignee`,`milestone`。
6. 点击 `Submit new issues`。

>用`CLI`创建`Issue`
1. 安装`gh`
```bash
#macOS(Homebrew)
brew install gh
#Linux(Debian/Ubuntu)
sudo apt install gh
#Windows(PowerShell)
winget install GitHub.cli
```
安装后需要重启终端或手动刷新环境变量
```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
```
```bash
# 重新加载用户配置文件
source ~/.bashrc   # 若你用 Bash
source ~/.zshrc    # 若你用 Zsh（macOS 新版默认）
```
或者直接刷新`PATH`环境变量
```bash
export PATH="$PATH:/usr/local/bin"  # 确保 gh 的安装目录在 PATH 中
```
安装后验证是否生效
```bash
gh --version
```
若输出版本号，说明环境变量已生效，可以继续执行`git auth login`

2. 登录`gh`(关联你的`GitHub`账号)
```bash
gh auth login
```
选择`GitHub.com`，然后一路回车，在`GitHub`的授权界面输入`PowerShell`中的8为验证码，再验证`GitHub`，即可建立连接。

3. 输入尝试
```bash
#进入你的练习仓库目录
cd ~/git-practice
```
```bash
# 创建 Issue（核心命令，可直接复制，替换标题/内容）
gh issue create \
  --title "feat: 新增用户列表功能" \
  --body "## 需求背景
为练习 GitHub 协作流程，需要在测试仓库中新增一个简单的用户列表功能。

## 需求内容
1. 创建 user_list.py 文件，实现用户列表获取和打印
2. 创建 USER_LIST_README.md 说明文档

## 验收标准
执行 python user_list.py 能正确输出用户列表" \
  --label "enhancement" \
  --assignee "你的GitHub用户名"
```
命令参数说明：
| 参数           | 作用                               | 示例                                       |
|----------------|------------------------------------|--------------------------------------------|
| `--title`      | Issue 标题                         | "feat: 新增用户列表功能"                   |
| `--body`       | Issue 详细描述（支持 Markdown）    | 上述模板内容                               |
| `--label`      | 给 Issue 打标签                    | "enhancement" / "bug" / "documentation"     |
| `--assignee`   | 指定负责人                         | 你的 GitHub 用户名                         |
| `--milestone`  | 关联里程碑（可选）                 | "v1.0"                                     |
4. 查看/管理`Issue`(CLI)
```bash
#查看当前仓库所有的Issue
gh issue list

#查看单个Issue详情(替换1为实际Issue编号)
gh issue view 1

#关闭Issue
gh issue close 1
```

### 1.6 Pull Request是什么？如何创建？
#### 一. PR是什么

`PR`是“把某个分支的改动合入目标分支”的提案。
可以在PR里让同学/同事`review`，再决定是否`merge`。
核心价值：
- 代码审查(Code Review)：让团队成员检查你的代码，提出改进建议，保证代码质量。
- 风险控制：避免直接向主分支(如`main`)推送代码，降低引入bug的风险
- 可追溯性：每一次合并都有明确的讨论】修改和审核记录，方便后续排查问题。
- 协作桥梁：将你的工作成果(代码)和团队的目标(主分支)连接起来。

#### 二.PR完整创建流程(Web端)
##### 1. 创建并推送功能分支
在创建PR之前，你需要现在本地完成开发，并将分支推送到远程仓库。
```bash
#1. 基于main分支创建并切换到功能分支
git chechout -b feature/login

#2. (开发代码，修改文件)

#3. 暂存并提交改动
git add .
git commit -m "feat: add login page"

#4.推从分支到远程，并建立追踪关系
git push -u origin feature/login
```
##### 2. 在网页端创建PR
1. 触发创建：推送成功后，GitHub仓库首页会出现一个醒目的绿色按钮`Compare & pull request`,直接点击即可。
2. 填写信息：
- 标题：简洁明了，最好关联Issue,例如`feat: add login page(#123)`。
- 描述：遵循“改了什么，为什么，怎么测”的原则详细说明，并加上`Close #123`来关联并自动关闭Issue。
3. 创建PR
- 点击`Create pull request`:创建一个正式的，可供审核的PR。

#### 三.CLI创建PR
>前提：已经推送到远端
```bash
# 确保你在功能分支上，并且已经推送到远程
gh pr create \
  --base main \
  --head feature/login \
  --title "feat: add login page (#123)" \
  --body "## 功能描述\n新增登录页面，实现手机号+验证码登录。\n\n## 关联 Issue\nCloses #123"
```
#### 四.PR与Issue的深度关系
- Issue 是 “问题 / 需求”：它定义了 “我们要做什么”，是任务的起点。
- PR 是 “解决方案代码”：它提供了 “我们如何做”，是任务的执行和交付。
- 自动关联：在 PR 的描述中使用 Closes #123、Fixes #123 或 Resolves #123 等关键词，当这个 PR 被成功合并到目标分支后，对应的 Issue #123 会被 GitHub 自动关闭，形成一个完整的闭环。

#### 五.合并PR
>当满足
1. 代码审查通过：所有指定的审查人（Reviewers）都已批准（Approved），没有未解决的 “请求修改”（Request changes）。
2. CI/CD 构建成功：如果仓库配置了自动化测试或构建流程（如 GitHub Actions），确保所有检查都已通过（显示绿色对勾）。
3. 无合并冲突：PR 页面没有提示 “合并冲突”（Merge conflicts）。如果有，必须先解决。
4. 分支是最新的：你的功能分支最好是基于最新的 main 分支开发的，避免合并后引入问题。

>条件后，在PR页面点击`Merge pull request`，会看到三种主要的合并选项
1. Create a merge commit（创建合并提交）
- 保留完整历史，内容较长
2. Squash and merge（压缩并合并）
- 清理历史，简洁
3. Rebase and merge（变基并合并）
- 最干净，有风险（不建议多人共享使用）

#### 六.解决合并冲突
如果你的功能分支和 main 分支在同一部分代码上都做了修改，GitHub 会提示 “无法自动合并”，这就是合并冲突。你必须手动解决它：
1. 在本地拉取并切换到你的功能分支：
```bash
git checkout feature/login
git pull origin feature/login
```
2. 从远程拉取最新的 main 分支代码：
```bash
git fetch origin
```
3. 在本地合并 main 分支到你的功能分支：
```bash
git merge origin/main
```
4. 解决冲突：
- Git 会在有冲突的文件中标记出冲突区域，格式如下：
```plaintext
<<<<<<< HEAD
// 这是 main 分支上的代码
console.log("Hello from main!");
=======
// 这是你功能分支上的代码
console.log("Hello from feature!");
>>>>>>> feature/login
```
- 你需要手动编辑文件，删除这些标记，并保留你认为正确的代码。
5. 提交解决后的代码：
```bash
git add .
git commit -m "resolve conflicts with main"
```
6. 推送回远程：
```bash
git push origin feature/login
```
#### 七.GitHub 协作最小工作流（建议记住）
1. 建一个Issue（明确目标）。
2. 新建功能分支开发。
3. 本地commit + push。
4. 提PR，邀请review。
5. 通过后merge，自动关闭Issue（若设置了 Closes #id）。