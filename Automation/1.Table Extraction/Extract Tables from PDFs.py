{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb50318d",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting camelot-py\n",
      "  Downloading camelot_py-0.10.1-py3-none-any.whl (40 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.0/41.0 KB\u001b[0m \u001b[31m57.2 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m0:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: chardet>=3.0.4 in /usr/lib/python3/dist-packages (from camelot-py) (4.0.0)\n",
      "Requirement already satisfied: click>=6.7 in /usr/lib/python3/dist-packages (from camelot-py) (8.0.3)\n",
      "Collecting openpyxl>=2.5.8\n",
      "  Downloading openpyxl-3.0.10-py2.py3-none-any.whl (242 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m242.1/242.1 KB\u001b[0m \u001b[31m1.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m[31m2.4 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting PyPDF2>=1.26.0\n",
      "  Downloading PyPDF2-2.4.0-py3-none-any.whl (197 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m197.3/197.3 KB\u001b[0m \u001b[31m334.9 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m[36m0:00:01\u001b[0mm eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting pdfminer.six>=20200726\n",
      "  Downloading pdfminer.six-20220524-py3-none-any.whl (5.6 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.6/5.6 MB\u001b[0m \u001b[31m793.0 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m0:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hCollecting tabulate>=0.8.9\n",
      "  Downloading tabulate-0.8.10-py3-none-any.whl (29 kB)\n",
      "Requirement already satisfied: numpy>=1.13.3 in /usr/lib/python3/dist-packages (from camelot-py) (1.21.5)\n",
      "Requirement already satisfied: pandas>=0.23.4 in /home/treviit/.local/lib/python3.10/site-packages (from camelot-py) (1.4.2)\n",
      "Collecting et-xmlfile\n",
      "  Downloading et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/lib/python3/dist-packages (from pandas>=0.23.4->camelot-py) (2022.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/lib/python3/dist-packages (from pandas>=0.23.4->camelot-py) (2.8.1)\n",
      "Collecting charset-normalizer>=2.0.0\n",
      "  Downloading charset_normalizer-2.1.0-py3-none-any.whl (39 kB)\n",
      "Collecting cryptography>=36.0.0\n",
      "  Downloading cryptography-37.0.2-cp36-abi3-manylinux_2_24_x86_64.whl (4.0 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.0/4.0 MB\u001b[0m \u001b[31m3.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting cffi>=1.12\n",
      "  Downloading cffi-1.15.0-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (446 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m446.3/446.3 KB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hCollecting pycparser\n",
      "  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)\n",
      "Installing collected packages: tabulate, PyPDF2, pycparser, et-xmlfile, charset-normalizer, openpyxl, cffi, cryptography, pdfminer.six, camelot-py\n",
      "Successfully installed PyPDF2-2.4.0 camelot-py-0.10.1 cffi-1.15.0 charset-normalizer-2.1.0 cryptography-37.0.2 et-xmlfile-1.1.0 openpyxl-3.0.10 pdfminer.six-20220524 pycparser-2.21 tabulate-0.8.10\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install camelot-py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5476d0c2",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting tk\n",
      "  Using cached tk-0.1.0-py3-none-any.whl (3.9 kB)\n",
      "Installing collected packages: tk\n",
      "Successfully installed tk-0.1.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install tk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "33fb1116",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting ghostscript\n",
      "  Downloading ghostscript-0.7-py2.py3-none-any.whl (25 kB)\n",
      "Requirement already satisfied: setuptools>=38.6.0 in /usr/lib/python3/dist-packages (from ghostscript) (59.6.0)\n",
      "Installing collected packages: ghostscript\n",
      "Successfully installed ghostscript-0.7\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install ghostscript"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cbe96461",
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'cv2'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_21695/228838063.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mcamelot\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mtables\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcamelot\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_pdf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'foo.pdf'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpages\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'1'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mflavor\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'lattice'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtables\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/camelot/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0m__version__\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0m__version__\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mio\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mread_pdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mplotting\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mPlotMethods\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/camelot/io.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mwarnings\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mhandlers\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mPDFHandler\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mutils\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mvalidate_input\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mremove_extra\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/camelot/handlers.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mcore\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mTableList\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mparsers\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mStream\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mLattice\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m from .utils import (\n\u001b[1;32m     11\u001b[0m     \u001b[0mTemporaryDirectory\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/camelot/parsers/__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mstream\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mStream\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mlattice\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLattice\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/camelot/parsers/lattice.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     23\u001b[0m     \u001b[0mcompute_whitespace\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m )\n\u001b[0;32m---> 25\u001b[0;31m from ..image_processing import (\n\u001b[0m\u001b[1;32m     26\u001b[0m     \u001b[0madaptive_threshold\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m     \u001b[0mfind_lines\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/camelot/image_processing.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# -*- coding: utf-8 -*-\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mcv2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'cv2'"
     ]
    }
   ],
   "source": [
    "import camelot\n",
    "\n",
    "tables = camelot.read_pdf('foo.pdf', pages='1', flavor='lattice')\n",
    "print(tables)\n",
    "\n",
    "tables.export('foo.csv', f='csv', compress=True)\n",
    "tables[0].to_csv('foo.csv')\n",
    "print(tables[0].df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
