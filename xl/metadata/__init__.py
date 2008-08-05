# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os

# do this so formats can inherit from stuff in _base
from _base import *

import aiff, asf, au, flac, mod, mp3, mp4, mpc, ogg, speex, tta, wav, wv

# lossy:    aac, mp2, mp3, speex, vorbis, wma
# lossless: flac, tta, wav, wavpack
# chip:     669, amf, dsm, far, it, med, mod, mtm, okt, s3m, stm, ult, xm
# other:    ac3, aiff, au, midi
# tags not read:  real, shorten (can we fix these?)
formats = {
        '669'   : mod.ModFormat,
        'aac'   : mp4.MP4Format,
        'ac3'   : None,
        'aif'   : aiff.AiffFormat,
        'aiff'  : aiff.AiffFormat,
        'amf'   : mod.ModFormat,
        'au'    : au.AuFormat, 
        'dsm'   : mod.ModFormat,
        'far'   : mod.ModFormat,
        'flac'  : flac.FlacFormat,
        'it'    : mod.ModFormat,
        'm4a'   : mp4.MP4Format,
        'med'   : mod.ModFormat,
        'mp2'   : mp3.MP3Format,
        'mp3'   : mp3.MP3Format,
        'mp4'   : mp4.MP4Format,
        'mid'   : None,
        'midi'  : None,
        'mod'   : mod.ModFormat,
        'mtm'   : mod.ModFormat,
        'oga'   : ogg.OggFormat,
        'ogg'   : ogg.OggFormat,
        'okt'   : mod.ModFormat,
        'ra'    : None,
        'ram'   : None,
        's3m'   : mod.ModFormat,
        'shn'   : None,
        'snd'   : au.AuFormat,
        'spx'   : speex.SpeexFormat,
        'stm'   : mod.ModFormat,
        'tta'   : tta.TTAFormat,
        'ult'   : mod.ModFormat,
        'wav'   : wav.WavFormat,
        'wma'   : asf.AsfFormat,
        'wv'    : wv.WavpackFormat,
        'xm'    : mod.ModFormat,
        }

# pass get_loc_for_io() to this.
def getFormat(loc):
    """
        get a Format object appropriate for the file at loc.
        if no suitable object can be found, a default object that
        defines title from the filename is used instead.
    """
    (path, ext) = os.path.splitext(loc.lower())
    ext = ext[1:] # remove the pesky .

    try:
        format = formats[ext]
    except KeyError:
        return None # not supported

    if format is None:
        format = BaseFormat

    return format(loc)

# vim: et sts=4 sw=4

