import asyncio
import pyshark
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import NetworkTraffic

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def wireshark_instructions(request):
    return render(request, 'wireshark_instructions.html')

def process_pcap(filepath):
    try:
        capture = pyshark.FileCapture(filepath)
        for packet in capture:
            try:
                print("*** line in for")
                NetworkTraffic.objects.create(
                    src_ip=packet.ip.src,
                    dst_ip=packet.ip.dst,
                    protocol=packet.transport_layer,
                    length=packet.length
                )
            except AttributeError as e:
                print(e)
                continue
    except Exception as e:
        print(e)
        raise e
    # finally:
    #     asyncio.gather(
    #         capture.close_async(),
    #         capture._get_tshark_process()
    #     )

        
def analyze_pcap(request):
    if request.method == 'POST' and request.FILES.get('pcap_file'):
        pcap_file = request.FILES['pcap_file']
        fs = FileSystemStorage()
        filename = fs.save(pcap_file.name, pcap_file)
        filepath = fs.path(filename)

        
        try:
            process_pcap(filepath)  # Await the async function directly


            # Fetch network traffic data after processing
            traffic = NetworkTraffic.objects.all()
            return render(request, 'analyze_pcap.html', {'traffic': traffic})

        except Exception as e:
            return HttpResponse(f"Error processing pcap: {str(e)}", status=500)
    
    return render(request, 'analyze_pcap.html')
