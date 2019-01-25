    1  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx cluster list
    2  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx cluster info bc20ddb243ba6090738e2cc951a03f7a
    3  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node info 38064f4566231705b8dcee1bba119bca
    4  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node info 38064f4566231705b8dcee1bba119bca
    5  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node info 38064f4566231705b8dcee1bba119bca
    6  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume info glusterfs-registry-volume
    7  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume list
    8  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume list | grep glusterfs-registry-volume
    9  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume info 6c063b886e91b4515739f79740e43c76
   10  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node list
   11  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx device add --name=/dev/sde --node=38064f4566231705b8dcee1bba119bca
   12  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx device add --name=/dev/sde --node=a44a0e7d8dbe55d78d9c6973c3fdeaeb
   13  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx device add --name=/dev/sde --node=cab3551ece01193ebab5ab4cdde371c4
   14  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume list
   15  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx noode list
   16  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node list
   17  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node info 38064f4566231705b8dcee1bba119bca
   18  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume list | grep registry
   19  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume info 6c063b886e91b4515739f79740e43c76
   20  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume expand -volume=6c063b886e91b4515739f79740e43c76 -expand-size=150
   21  heketi-cli volume expand --help
   22  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume expand --volume 6c063b886e91b4515739f79740e43c76 --expand-size 150
   23  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx node info 38064f4566231705b8dcee1bba119bca
   24  heketi-cli --server http://localhost:8080 --user admin --secret xxxxxxxxxxx volume expand --volume 6c063b886e91b4515739f79740e43c76 --expand-size 50 
