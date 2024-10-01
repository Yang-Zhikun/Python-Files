import os

print("一键生成vscode的C/C++配置文件\n")
print("先决条件：\n\t1.安装vscode并安装C/C++扩展\n\t2.安装MinGW64\n\n")

workspacePath = input("请输入工作区路径，或者把工作区的文件夹拖进来：\n")
#在路径中的反斜杠'\'改为正斜杠'/'
workspacePath = workspacePath.replace('\\', '/')

mingwPath = input("输入编译器MinGW64的路径，或者把MinGW64的文件夹拖进来(如D:\\MinGW64)：\n")
#在路径中的反斜杠'\'改为正斜杠'/'
mingwPath = mingwPath.replace('\\', '/')

# 检查并创建.vscode目录
vscode_dir = os.path.join(workspacePath, ".vscode")
if not os.path.exists(vscode_dir):
    os.makedirs(vscode_dir)

# 生成配置文件c_cpp_properties.json
with open(os.path.join(vscode_dir, "c_cpp_properties.json"), "w") as f:
    f.write(r"""{
        "configurations": [
            {
                "name": "Win32",
                "includePath": [
                    "${workspaceFolder}/*/*"
                ],
                "defines": [
                    "_DEBUG",
                    "UNICODE",
                    "_UNICODE"
                ],
                "cStandard": "c11",
                "cppStandard": "c++11",
                "intelliSenseMode": "windows-gcc-x64",
                "compilerPath": "%s/bin/g++.exe"
            }
        ],
        "version": 4
    }
""" % mingwPath)

# 生成配置文件tasks.json
with open(os.path.join(vscode_dir, "tasks.json"), "w") as f:
    f.write(r"""
{
	"version": "2.0.0",
	"tasks": [

		{
			"type": "cppbuild",
			"label": "C/C++: g++.exe build active file",
			"command": "%s/bin/g++.exe",
			"args": [
				"-fdiagnostics-color=always",
				"-std=c++11", //c++11标准
				"-g",
				"${file}",
				"-o",
				"${workspaceFolder}/.exe/a.exe",
				"-leasyx",
				"-lwinmm",
			],
			"options": {
				"cwd": "%s/bin"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"detail": "compiler: %s/bin/g++.exe"
		}		
	]
}
""" % (mingwPath, mingwPath, mingwPath))

# 生成配置文件launch.json
with open(os.path.join(vscode_dir, "launch.json"), "w") as f:
    f.write(r"""
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "C/C++: g++.exe build and debug active file",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/.exe/a.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                },
            ],
            "miDebuggerPath": "%s/bin/gdb.exe",
            "preLaunchTask": "C/C++: g++.exe build active file"
        }
    ]
}
"""%mingwPath)
    
# 生成配置文件settings.json
with open(os.path.join(vscode_dir, "settings.json"), "w") as f:
    f.write(r"""
{
    "files.autoSave": "afterDelay",
    "files.encoding": "gbk",
    "C_Cpp.errorSquiggles": "enabled"
}
""")

print("配置文件生成完毕")
