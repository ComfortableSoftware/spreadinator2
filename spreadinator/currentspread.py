

from . import(
  VARS as V,
)


locals().update(V.CF_OS.ALL_THE_OS_DATA)
locals().update(V.ALL_THE_SPREAD_VALS)


WAIS = V.CF_WW.whereStr


def checkDirs():
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  _TList1_ = V.CF_OS.globDirList(rootDir_="./")
  #print(f"""{_TList1_=}""")
  for _thisDirStr_ in _TList1_:
    # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (
        (_thisDirStr_[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    ):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      V.CF_OS.MV(
        _thisDirStr_,
        f"""z{_thisDirStr_}"""
      )
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1



def main():
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  #with V.CF_LOG.LOG_FILE_C(filename_=V.ACTIVE_LOG_URL) as V.LOG:
  with V.CF_LOG.LOG_FILE_C(
      dir_=V.VCD[KD_LOG_DIR],
      filename_=V.VCD[KD_LOG_FILENAME],
    ) as V.LOG:
    # 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    checkDirs()
    V.LOGW = V.LOG.write
    V.PLE.reset()
    V.PLE.DIRS_ONLY = True
    V.PLE.FILES_ONLY = False
    V.PLE.PATH = V.VCD[KD_DEST_DIR]
    V.PLE.fillDirs()
    _status_, _numFiles_ = V.CF_OS.getFCount(rootDirToCount_=V.VCD[KD_DEST_DIR])

    if (
        (_status_ is not True)
    ):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      _strToWrite_ = f"""Something broke.{NEWLINE}getFCount returned {_numFiles_}"""
      V.LOGW(_strToWrite_, printToo_=False)
      V.CF_OS.EXIT(53)
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
    _numFiles_ = int(_numFiles_)

    if (
        (V.VCD[KD_NUM_DEST_DIRS] != 0)
    ):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      # V.VCD[KD_NUM_DEST_DIRS] += 1
      _numFilesPerDir_ = (_numFiles_ / V.VCD[KD_NUM_DEST_DIRS])
      _numDirs_ = V.VCD[KD_NUM_DEST_DIRS]
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
    elif (
        (V.VCD[KD_FILES_PER_DIR] != 0)
    ):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      _numFilesPerDir_ = V.VCD[KD_FILES_PER_DIR]
      _numDirs_ = int(_numFiles_ / _numFilesPerDir_) + 1
      V.setCurrentStuff(
          numDestDirs_=_numDirs_,
        )
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
    else:
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      print(f"""The world is broken """)
      _strToWrite_ = f"""The world is broken{NEWLINE}I'm stopping everything
      I need either -n {V.VCD[KD_NUM_DEST_DIRS]} or -cspread {V.VCD[KD_FILES_PER_DIR]} to work out to sane numbers"""
      V.LOGW(_strToWrite_)
      V.CS_OS.EXIT(53)
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3

    _strToWrite_ = f"""I found {_numFiles_} total files, which will be put into {_numDirs_} with {_numFilesPerDir_} per directory"""
    V.LOGW(_strToWrite_)

    V.checkMakeDest(
        forCWD_=True,
      )

    for _thisDir_ in V.TQ_DM(V.PLE.DL, position=0, colour="#Cf2fBf", leave=True, desc="DIRS…"):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      _strToWrite_ = f"""Gathering files in '{_thisDir_[K_PATH]}'{NEWLINE}"""
      V.LOGW(_strToWrite_)
      V.PLE.resetFiles()
      _thisDirStr_ = _thisDir_[K_PATH]
      #print(f"""{WAIS()}Finding files in '{_thisDirStr_}'""")
      V.PLE.DIRS_ONLY = False
      V.PLE.FILES_ONLY = True
      V.PLE.PATH = _thisDirStr_
      V.PLE.fillFiles()
      #print(f"""Found {_numFiles_} files to process.""")
      _thisNumFiles_ = V.PLE.FL.__len__()

      if (
          (_thisNumFiles_ < 1)
      ):
        # 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
        continue
        # ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4

      _strToWrite_ = f"""Starting on {_thisNumFiles_} of {_numFiles_} files that will go into {V.VCD[KD_NUM_DEST_DIRS]} with {_numFilesPerDir_} per directory."""
      V.LOGW(_strToWrite_, printToo_=False)
      #_strToWrite_ = """The current file list is"""
      #for _thisFileEntry_ in V.PLE.FL:
      #  _strToWrite_ += f"""'{_thisFileEntry_[K_PATH]}'{NEWLINE}"""
      #V.LOGW(_strToWrite_)
      #exit()


      for _thisFileEntry_ in V.TQ_DM(V.PLE.FL, position=1, colour="#4f3fff", leave=False, desc="FILES"):
        # 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱

        if (
            (V.VCD[KD_RENAME] is True)
        ):
          # 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
          _TStr_ = V.CF_HASH.doAHash(hash_=V.VCD[KD_HASH], stringToHash_=_thisFileEntry_[K_PATH])
          # ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
        else:
          # 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
          _TStr_ = _thisFileEntry_[K_JUST_FILENAME]
          # ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5

        _thisFileEntry_ = V.CF_OS.addNewFilePiece(
            thisFileEntry_=_thisFileEntry_,
            newDir_=f"""{V.VCD[KD_DEST_DIR]}/{V.VCD[KD_DIR_NUM]:{V.VCD[KD_NUM_DIR_DIGITS_STR]}}""",
            newExtension_=_thisFileEntry_[K_EXTENSION],
            newJustFilename_=_TStr_,
          )

        _strToWrite_ = f"""Move '{_thisFileEntry_[K_PATH]}' to '{_thisFileEntry_[K_NEW_PATH]}'"""
        V.LOGW(_strToWrite_, printToo_=False)
        V.CF_OS.MV(
          _thisFileEntry_[K_PATH],
          _thisFileEntry_[K_NEW_PATH],
        )
        V.INC_DIR_NUM()
        # ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3
    # ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1








#
