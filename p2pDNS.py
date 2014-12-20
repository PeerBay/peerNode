import libtorrent as lt
import time


piece_size = 256 * 1024
creator_str = "peerbay.p2p"
thetracker = "bttracker.debian.org"
theurlseed = "your desired url seed"

fs = lt.file_storage()
lt.add_files(fs, "demoCA")
fs.num_files()

t = lt.create_torrent(fs, piece_size)
t.add_tracker(thetracker)
lt.set_piece_hashes(t, ".")
t.set_root_cert("newkey.pem")
t.set_creator(creator_str)
#~ t.add_url_seed(theurlseed)

f = open("dom.torrent", "wb")
f.write(lt.bencode(t.generate()))
f.close()
ses = lt.session()
ses.listen_on(6881, 6891)


e = lt.bdecode(open("dom.torrent", 'rb').read())
info = lt.torrent_info(e)

params = { "save_path": './', \
        "storage_mode": lt.storage_mode_t.storage_mode_sparse, \
        "ti": info }
h = ses.add_torrent(params)
while True:
        s = h.status()

        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']
        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state])

        time.sleep(1)
