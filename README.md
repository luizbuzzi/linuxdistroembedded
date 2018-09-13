# linuxdistroembedded

USO

É preciso configurar a interface de rede, para isso abra o arquivo com o seu editor preferido e substitua o IP do host pelo IP do com putador

./buildroot/custom-scripts/S41network-config

Edite as linhas /sbin/route add -host <IP-DO-HOST> dev eth0
  	            /sbin/route add default gw <IP-DO-HOST>

Para instalar entre na pasta buildroot e digite o comando:

make

Para inicializar monte a imagem do sistema com o seguinte comando:

$ mount -o loop output/images/rootfs.ext2 ../rootfs/

Após o comando anterior, configure o IP de rede digitando o seguinte:

sudo qemu-system-i386 --device e1000,netdev=eth0,mac=aa:bb:cc:dd:ee:ff \
  	--netdev tap,id=eth0,script=custom-scripts/qemu-ifup \
  	--kernel output/images/bzImage \
  	--hda output/images/rootfs.ext2 \
  	--nographic \
  	--append "console=ttyS0 root=/dev/sda"     
    
    
TUTORIAL

Considerando que os tutoriais de buildroot e configuração de rede já tenham sido realizados, partimos dos seguintes passos abaixo. 

Crie um diretório com o comando abaixo:

./buildroot/custom-scripts/mon-server

Crie um arquivo com o seu editor de sua preferência no endereço abaixo:

./buildroot/custom-scripts/mon-server/server.py

Copie o código abaixo dentro do arquivo e salve:






