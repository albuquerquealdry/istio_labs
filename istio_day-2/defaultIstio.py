import os
from tabnanny import check

def checkIstio():
    os.system ("cd istio-1.13.3 && export PATH=$PWD/bin:$PATH")
    os.system("cd istio-1.13.3  && istioctl install --set profile=demo -y" )
    os.system("cd istio-1.13.3  && kubectl label namespace default istio-injection=enabled")
    os.system("cd istio-1.13.3  && kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml")

checkIstio()