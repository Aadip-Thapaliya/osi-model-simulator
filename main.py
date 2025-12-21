from utils.logger import configure_logging
from core.application import ApplicationLayer
from core.presentation import PresentationLayer
from core.session import SessionLayer
from core.transport import TransportLayer
from core.network import NetworkLayer
from core.datalink import DataLinkLayer
from core.physical import PhysicalLayer


def main():
    configure_logging(verbose=False)

    print("Aadip Thapaliya | 92710466 | UE Applied Sciences\n")

    message = input("Enter message: ")

    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    dl = DataLinkLayer()
    phy = PhysicalLayer()

    data = app.send(message)
    data = pres.send(data)
    data = sess.send(data)
    data = trans.send(data)
    data = net.send(data)
    data = dl.send(data)
    data = phy.send(data)

    frames = phy.receive(data)
    packets = dl.receive(frames)
    segments = net.receive(packets)
    data = trans.receive(segments)
    data = sess.receive(data)
    data = pres.receive(data)
    data = app.receive(data)

    print("\nRecovered message:", data)

if __name__ == "__main__":
    main()
