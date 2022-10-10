
- just for diao-min  
### Python with PyQt5
***Some English Text is translated by me, But my English scores is not very well***  

<a href="#english">Englist Text(translated by [here](https://cn.bing.com/search?q=google%E7%BF%BB%E8%AF%91&cvid=fa59938cb75f45d5b083539b611bd930&aqs=edge.2.69i57j0l7j69i61.5509j0j1&pglt=171&FORM=ANNTA1&PC=U531))<br>click it to read the englist text</a>

我使用pyqt5制作了它，也算是一个游戏吧。  
`结合了requests请求库。`

也就只是一个爬虫，一个爬图片的爬虫而已（核心逻辑）。  
在“save/image”里是所下载的图片，用于显示。


<img src="https://api.ixiaowai.cn/api/api.php" width="300" height="200"><img src="<https://api.mtyqx.cn/tapi/random.php>  " width="300" height="200">  
  
从  
  
  <https://api.ixiaowai.cn/api/api.php>   
    
  <https://api.mtyqx.cn/tapi/random.php>  
    
  <https://api.mtyqx.cn/api/random.php>  
    
  <https://www.dmoe.cc/random.php>  
    
  <https://cdn.seovx.com/d/?mom=302>  
    
  <https://img.paulzzh.com/touhou/random?size=all>  
      
下载  
<strong> 问题：nuitka 打包出现问题，我经常在这失败。请求帮助。</strong>  
***安装过程见<a href="#code">这里</a>***
***如果你想要提供帮助，请发送邮件到<903954856@qq.com>***
 
  
  

<p id="english"><br>
  
I made it with pyqt5, and it's a game.<br>
Combined with requests request library<br>
It's just a crawler, a crawler that crawls pictures (core logic)<br>
In "save/image" is the downloaded image for display.<br>
<strong>Only Chinese are supported</strong>
  download from  
  
  <https://api.ixiaowai.cn/api/api.php，>   
    
  <https://api.mtyqx.cn/tapi/random.php，>  
    
  <https://api.mtyqx.cn/api/random.php，>  
    
  <https://www.dmoe.cc/random.php，>  
    
  <https://cdn.seovx.com/d/?mom=302，>  
    
  <https://img.paulzzh.com/touhou/random?size=all>  
      


</p>
<strong> Problem: There is a problem with nuitka packaging, and I often fail here. i always fail. Please help me.</strong>

<code id="code">  
<h3 id="code">nuitka</h3>
C:\Users\dell>cd C:\Users\dell\Desktop\..py\PyQt\Project\c-i
C:\Users\dell\Desktop\..py\PyQt\Project\c-i>nuitka main.py
Nuitka-Options:INFO: Used command line options: main.py
Nuitka-Options:WARNING: You did not specify to follow or include anything but main
Nuitka-Options:WARNING: program. Check options and make sure that is intended.
Nuitka:WARNING: Using very slow fallback for ordered sets, please install 'ordered-set'
Nuitka:WARNING: PyPI package for best Python compile time performance.
Nuitka:INFO: Starting Python compilation with Nuitka '1.0.7' on Python '3.10' commercial grade 'not installed'.
Nuitka:INFO: Completed Python level compilation and optimization.| 1/1, __main__
Nuitka:INFO: Generating source code for C backend compiler.
Nuitka:INFO: Running data composer tool for optimal constant value handling.
Nuitka:INFO: Running C compilation via Scons.
Nuitka-Scons:INFO: Backend C compiler: gcc (gcc).
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [static_src\CompiledGeneratorType.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [static_src\MainProgram.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [static_src\CompiledCellType.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [static_src\CompiledFunctionType.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [__constants.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [__helpers.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

                                               scons: *** [module.__main__.o] Error 1
gcc.exe: error: CreateProcess: No such file or directory

Backend C: 88.9%|██████████████████████▏  | 8/9scons: *** [__loader.o] Error 1

C:\Users\dell\Desktop\..py\PyQt\Project\c-i>
</code>
***If you would like to help, please send an email to <903954856@qq.com>***
