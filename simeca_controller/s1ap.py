#Copyright Binh Nguyen University of Utah (binh@cs.utah.edu)
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.


#
#S1AP message.
#
class S1AP:
    def __init__(self, pkt_number=-1, msg_text="", ue_mme_id = "", ue_enb_id="", nas=None):
        self.pkt_number = pkt_number
        self.msg_text = msg_text
        self.ue_enb_id = ue_enb_id
        self.nas = nas
        self.ue_mme_id = ue_mme_id

    def print_all(self):
        print "pkt# = %s\n" %self.pkt_number
        print "msg_text = %s\n" %self.msg_text
        print "ue_enb_id = %s\n" %self.ue_enb_id
        print "ue_mme_id = %s\n" %self.ue_mme_id
        self.nas.print_all()

class InitiatingMsg:
    def __init__(self,  ue_enb_id = "", ue_imsi = "", enb_cellid = ""):
        self.ue_enb_id = ue_enb_id
        self.ue_imsi = ue_imsi
        self.enb_cellid = enb_cellid

 
