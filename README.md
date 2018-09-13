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

Após isso, o sistema já vai estar rodando, podendo ser acessado pelo host em um navegador de sua preferência com o link:

http://192.168.1.10:8080
