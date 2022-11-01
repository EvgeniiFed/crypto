## To set up bot you will need: 

### • Linux system
---
it have to be online so I recommend to run bot in remote server, of course you can use your home PC  if you okay 
<details> 
  <summary>If you don't know how to get one </summary> ㅤ
  
   ㅤ• **[Digital Ocean](https://link.web3topia.wtf/DigitalOcean)** is expencive, but by this [link](https://link.web3topia.wtf/DigitalOcean) you will get 200$ trial for 2 months. So it up to 3 VPS free for 2 month - great choise to start, but i would not suggest to pay there.
   
   ㅤ• **[Contabo](https://contabo.com/)** is cheapest VPS - for bot absoulutelly ok
   
   ㅤ• **[Hetzner](https://www.hetzner.com/)** - best quality/price balance (probably optimal for nodes)  
  
</details>


You will need some dependences to run bot. 
Run  command block below to update your system and install them

    cd $HOME
    sudo apt update && sudo apt upgrade -y
    apt install tmux python3-pip -y
    pip3 install getch loguru requests

### • Bot token from BotFather
---
<details> 
  <summary>If you don't know how to get one </summary> ㅤ
  
  ㅤ• go to [BotFather bot](https://t.me/BotFather) and create new bot 
    ㅤ![](https://i.ibb.co/h2bRBP2/Screenshot-55.png)
  ㅤ
   
</details>

    DG_TOKEN=PASTE YOUR TELEGRAM BOT TOKEN HERE

### • Discord token
---
<details> 
  <summary>If you don't know how to get one </summary> ㅤ
  
  ㅤ•  
  
</details>

    DS_TOKEN=PASTE YOUR DISCORD TOKEN HERE


