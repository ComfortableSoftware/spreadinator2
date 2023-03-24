

from . import (
    UTILS as U,
    VARS as V,
  )


locals().update(V.ALL_THE_SPREAD_VALS)
locals().update(V.CF_OS.ALL_THE_OS_DATA)


def main():
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  CC = V.CF_CNT(high_=V.NUM_FILES)
  CN = CC.N
  with V.CF_LOG.LOG_FILE_C(
        dir_=V.ACTIVE_LOG_DIR,
        filename_=V.ACTIVE_LOG_FILENAME,
      ) as V.LOG:
    V.LOGW = V.LOG.write
    #V.LDC.reset()
    #V.LFC.reset()
    V.PLC.reset()
    #print(f"""{WAIS()}Scanning all {len(V.VCD[KD_SOURCE_DIR_LIST])} directories and adding directories found.""")
    for _thisDir_ in V.TQ_DM(V.VCD[KD_SOURCE_DIR_LIST], position=0, colour="#6f0f9f", leave=True, desc=f"""{PD(STP_="ROOT")}"""):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      _strToWrite_ = f"""Processing root directory '{_thisDir_}'{NEWLINE}"""
      V.LOGW(_strToWrite_)
      _previousDirCount_ = len(V.PLC.DL)
      #print(f"""{WAIS()}Scanning for all directories in the root tree {_thisDir_}""")
      V.PLC.DIRS_ONLY = True
      V.PLC.FILES_ONLY = False
      V.PLC.PATH = _thisDir_
      V.PLC.fillDirs()
      _newDirCount_ = len(V.PLC.DL)
      _dirCountDifference_ = _newDirCount_ - _previousDirCount_
      _strToWrite_ = f"""I found {_dirCountDifference_} directories and added them to the list.{NEWLINE}"""
      V.LOGW(_strToWrite_)
      # ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3 ⟰3

    _strToWrite_ = f"""Found {len(V.PLC.DL)} subdirectories in all root directories.{NEWLINE}"""
    V.LOGW(_strToWrite_)

    for _thisDir_ in V.TQ_DM(V.PLC.DL, position=0, colour="#Cf2fBf", leave=True, desc=f"""{PD(STP_="SUBDIR")}"""):
      # 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱ 3⟱
      _strToWrite_ = f"""Gathering files in '{_thisDir_[K_PATH]}'{NEWLINE}"""
      V.LOGW(_strToWrite_)
      V.PLC.resetFiles()
      _thisDirStr_ = _thisDir_[K_PATH]
      #print(f"""{WAIS()}Finding files in '{_thisDirStr_}'""")
      V.PLC.DIRS_ONLY = False
      V.PLC.FILES_ONLY = True
      V.PLC.PATH = _thisDirStr_
      V.PLC.fillFiles()
      _numFiles_ = len(V.PLC.FL)
      #print(f"""Found {_numFiles_} files to process.""")

      if (
          (_numFiles_ < 1)
      ):
        # 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
        continue
        # ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4

      for _thisFileEntry_ in V.TQ_DM(V.PLC.FL, position=1, colour="#4f3fff", leave=False, desc=f"""{PD(STP_="FILES")}"""):
        # 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱ 4⟱
        if (
            (V.VCD[KD_RENAME] is True)
        ):
          # 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
          _TName_ = V.hashName(
            thisFileEntry_=_thisFileEntry_,
          )
          # ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
        else:
          # 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱ 5⟱
          _TName_ = _thisFileEntry_[K_JUST_FILENAME]
          # ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
        _thisFileEntry_ = V.CF_OS.addNewFilePiece(
            newDir_=f"""{V.VCD[KD_DEST_DIR_COPY]}/{V.VCD[KD_DIR_NUM]:{V.VCD[KD_NUM_DIR_DIGITS_STR]}}""",
            newExtension_=_thisFileEntry_[K_EXTENSION],
            newJustFilename_=_TName_,
            thisFileEntry_=_thisFileEntry_,
          )
        _copyResult_ = U.doCopyAFile(
            destURL_=_thisFileEntry_[K_NEW_PATH],
            sourceURL_=_thisFileEntry_[K_PATH],
          )

        if (
            (_copyResult_[0] is True)
        ):
          # V.INC_DIR_NUM()

          # ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5 ⟰5
        # ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4 ⟰4



#
