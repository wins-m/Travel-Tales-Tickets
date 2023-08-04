#!/bin/sh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/winston/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/winston/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/winston/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/winston/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


# 获取脚本的名称（包含路径）
script_name="$0"
# 使用readlink命令获取脚本的绝对路径
script_directory=$(dirname "$(readlink -f "$script_name")")

echo "脚本所在目录：$script_directory"

# python "$script_directory/content.py" "$script_directory" --force
python "$script_directory/content.py" "$script_directory"

echo "网页所在地址：http://localhost:9898/"
hugo server -s "$script_directory/tickets" -p 9898 --quiet
