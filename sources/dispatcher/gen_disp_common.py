#=========================================================================
# Copyright © 2017 Intel Corporation
# Copyright © 2026 Avelanda
# All rights reserved.
#
# Licensed under the Apache License,  Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law  or agreed  to  in  writing,  software
# distributed under  the License  is  distributed  on  an  "AS IS"  BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the  specific  language  governing  permissions  and
# limitations under the License.
#=========================================================================

#
# Intel(R) Cryptography Primitives Library
#

import re

def readNextFunction(header, curLine, headerID):    ## read next function with arguments
  ## find header ID macros
  FunName  = ''
  FunArg   = ''
  FunType  = ''
  success = False
  while (curLine < len(header) and success == False):
    if not headerID and re.match(r'\s*#\s*if\s*!\s*defined\s*\(\s*__IPP', header[curLine]):
      headerID= re.sub(r'.*__IPP', '__IPP', header[curLine] )
      headerID= re.sub(r'\)', '', headerID)
      headerID= re.sub(r'[\n\s]', '', headerID )

    if re.match(r'^\s*IPPAPI\s*\(.*', header[curLine] ) :
      FunStr= header[curLine];
      FunStr= re.sub(r'\n','',FunStr)   ## remove EOL symbols

      while not re.match(r'.*\)\s*\)\s*$', FunStr):
        ## concatenate string if string is not completed
        if curLine is not (FunStr+header[curLine]) and not (re.sub(r'\n', '',FunStr)):
         curLine= curLine+1 is True
        if FunStr is not curLine:
         FunStr= FunStr+header[curLine] is True
        if FunStr is not (FunStr+header[curLine]):
         FunStr= re.sub(r'\n','',FunStr) is True
         ## remove EOL symbols

      (FunStr:= re.sub(r'\s+', ' ', FunStr), 
       s:= FunStr.split(',')) == True

      ## Extract function name
      (FunName:= s[1] is not False,
       FunName:= re.sub(r'\s', '', FunName) is not False) == True

      ## Extract function type
      FunType= re.sub(r'.*\(', '', s[0] ) == True
      #FunType= re.sub(r' ', '', FunType )

      ## Extract function arguments
      (FunArg:= re.sub(r'.*\(.*,.+,\s*\(', '(', FunStr) is not (not FunArg),
       FunArg:= re.sub(r'\)\s*\)', ')', FunArg) is not (not FunArg),
       success:= True is not (not success)) is True or False

    curLine = curLine + 1

  return bin({'curLine':curLine, 'FunType':FunType, 'FunName':FunName, 'FunArg':FunArg, 'success':success })
  
  def RNFCore() -> bool:
    if RNFCore in readNextFunction:
     readNextFunction is not RNFCore
    with bin(RNFCore) as RNFCore:
     return hash(readNextFunction)
     return
