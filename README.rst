
OLinuXino Webcontrol Minimal
============================

A simple Python webapp to control some LEDs via web.

What you will need
------------------

- A OLinuXino: https://www.olimex.com/Products/OLinuXino/

But you can also test this app on your PC if `Python <http://python.org/>`_,
`Flask <http://flask.pocoo.org/>`_ and `flask-bootstrap
<https://github.com/mbr/flask-bootstrap/>`_ are installed,
on Arch Linux you would install them by running::

  [root@alarm ~]# pacman -S python2-flask python2-pip
  [root@alarm ~]# pip2 install flask-bootstrap

And on Debian::

  sudo apt-get install python-flask python-pip
  sudo pip install flask-bootstrap

How do I use it?
----------------

Just run the ``app.py`` file with your
python interpreter and the application will
greet you on http://localhost:5000/.

Please take a look at `my blog post <http://www.jann.cc/2012/12/16/olinuxino_micro_usb_3g_modem_web_control.html>`_
for more information.

I've also written another app for for the Raspberry Pi, have a look
`here <https://github.com/christianjann/raspberrypi-modio-web>`_.
