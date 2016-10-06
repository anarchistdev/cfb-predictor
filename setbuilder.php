<?php

include 'simple_html_dom.php';
include 'team.php';

class SetBuilder {

    public $team;
    private $teamStr;
    
    public function __construct($teamStr) {
        $this->team = new Team();
        $this->teamStr = $teamStr;
	}

    public function buildSet() {
    
        $url = "http://www.sports-reference.com/cfb/schools/" . $this->teamStr . "/2016.html";
        $contents = file_get_html($url);
        $this->team->name = $this->teamStr;

        foreach($contents->find('p') as $element) { // for each <p>
            $text = $element->plaintext; // get the plain text of the element
            
            // find record
            if (strtok($text, " ") === 'Record:') {
                $record = preg_replace('/(Record:)/', '', $text);
                $this->team->wins = $this->getWins(trim($record));
                $this->team->losses = $this->getLosses(trim($record));
            } 
            
            // find conference
            if (strtok($text, " ") === 'Conference:') {
                $conf = preg_replace('/(Conference:)/', '', $text);
                $this->team->conf = trim($conf);
            }
            
            // find ranking
            if (strtok($text, " ") === 'Rank:') {
                $rnk = preg_replace('/(Rank:)/', '', $text);
                $this->team->rank = $this->getRank(trim($rnk));
            } else {
                if (!isset($this->team->rank)) {
                    $this->team->rank = 0; // If unranked, set to 0.
                }
            }
            
            // find sos
            if (strtok($text, " ") === 'SOS:') {
                $ss = preg_replace('/(SOS:)/', '', $text);
                $this->team->sos = trim($this->getSOS(trim($ss)));
            }

            // Find the average points per game
            if (strtok($text, " ") === 'Points/G:') {
                $txt = trim($this->getSOS(trim($text)));
                $ppg = preg_replace('([^0-9.]+)', '', $txt);
                $this->team->ppg = $ppg;
                //echo $ppg;
            }
            
        }
        
        // count the number of injuries
        foreach ($contents->find('table') as $element) {
            if (trim($element->id) == 'injuries') {
                foreach($element->find('td') as $row) {
                    if (strpos($row->plaintext, 'Out') !== false) {
                        $this->team->numInjuries++;
                    }
                }
            }
        }

        // TODO - combine this foreach with the inj. 

        // Collect yardage data
        foreach($contents->find('table') as $element) {
            if (trim($element->id) == 'team') {
                foreach($element->find('td') as $row) {
                
                    // Collect rushing info
                    if ($row->getAttribute("data-stat") === "rush_yds_per_att") {
                        if (!isset($this->team->avgRushYds)) {
                            $this->team->avgRushYds = $row->plaintext;
                        }
                    } else if ($row->getAttribute("data-stat") === "opp_rush_yds_per_att") {
                        if (!isset($this->team->avgDefRush)) {
                           $this->team->avgDefRush = $row->plaintext; 
                        }
                    }
                    
                    // Collect passing info
                    if ($row->getAttribute("data-stat") === "pass_cmp") {
                        if (!isset($this->team->passCmp)) {
                            $this->team->passCmp = $row->plaintext;
                        }
                    } else if ($row->getAttribute("data-stat") === "pass_att") {
                        if (!isset($this->team->passAtt)) {
                            $this->team->passAtt = $row->plaintext;
                        }
                    } else if ($row->getAttribute("data-stat") === "pass_yds") {
                        if (!isset($this->team->passYds)) {
                            $this->team->passYds = $row->plaintext;
                        }
                    } else if ($row->getAttribute("data-stat") === "tot_yds") {
                        if (!isset($this->team->totalYds)) {
                            $this->team->totalYds = $row->plaintext;
                        } 
                    }
                    
                }
            }
        }
        

    }

    private function getWins($str) {
        $pattern = "/([0-9])-/";
        preg_match($pattern, $str, $matches);
        return preg_replace('/(-)/', '', $matches[0]);
    }

    private function getLosses($str) {
        $pattern = "/-([0-9])/";
        preg_match($pattern, $str, $matches);
        return preg_replace('/(-)/', '', $matches[0]);
    }

    private function getRank($str) {
        $pattern = "/(^[0-9]*[0-9])/";
        preg_match($pattern, $str, $matches);
        return $matches[0];
    }
    
    private function getSOS($str) {
        $pattern = "/(.*?)\(.*\)+/";
        preg_match($pattern, $str, $matches);
        return $matches[1];
    }

}


?>
