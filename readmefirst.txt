这是我个人的python脚本库。
This is my own python scripts box.



关于smartgit的说明：

?右键第一个版本的记录，选择Reset可以回归到这个版本。Reset有三种模式可以选择，mixed、soft、hard。
 
mixed：工作区不变，reset暂存区、reset当前分支
 
soft：工作区不变、暂存区不变、reset当前分支
 
hard：reset工作区、reset暂存区、reset当前分支



多分支管理

Git鼓励大量使用分支：
查看分支：git branch 
创建分支：git branch <name> 
切换分支：git checkout <name> 
创建+切换分支：git checkout -b <name> 
合并某分支到当前分支：git merge <name> 
删除分支：git branch -d <name>