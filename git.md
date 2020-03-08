## Git

git checkout develop
git merge --no-ff 2_5_4_basic
git push origin develop



git config --global user.name "liqiong"
git config --global user.email "liqiong456@126.com"
ssh-keygen -t rsa -C "liqiong456@126.com" 


git config --global credential.helper store


.gitignore 忽略文件没有作用
git rm -r --cached .
git add .
git commit -m 'update .gitignore'