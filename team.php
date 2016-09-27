<?php

class Team {
    public $wins;
    public $losses;
    public $conf;
    public $numInjuries = 0;
    public $rank;
    public $sos; // sos - strength of schedule
    public $name;
    
    // TODO - make these values automated, pulled from different data
    // sources.
    public $conferences = array (
        "ACC (Atlantic Division)"  => 20,
        "ACC (Coastal Division)" => 15,
        "SEC (East Division)"   => 20,
        "SEC (West Division)"   => 20,
        "Big 12" => 15,
        "Sun Belt" => 10,
        "Ind" => 12
    );
    
    public function generatePoints() {
        $confPoints = $this->conferences[trim($this->conf)];
        $lossPoints = -($this->losses * 5);
        $winnPoints = $this->wins * 3;
        
        $rankPoints = 0;
        if ($this->rank != 0) {
            $rankPoints = $this->rank / 3;
        } else {
            $rankPoints = 15;
        }
        
        return $confPoints + ($lossPoints + $winnPoints) - $rankPoints;
    }
    
}

?>
