<?php

class Team {
    public $wins;
    public $losses;
    public $conf;
    public $numInjuries = 0;
    public $rank;
    public $sos; // sos - strength of schedule
    public $name;
    
    
    public function export() {
        $fileName = "sets/" . $this->name . ".txt";
        $file = file_get_contents($fileName);
        $line1 = "wins: ". $this->wins;
        $line2 = "losses: ". $this->losses;
        $line3 = "conf: ". $this->conf;
        $line4 = "rank: ". $this->rank;
        $line5 = "sos: ". $this->sos;
        $line6 = "numInj: ". $this->numInjuries;
        
        $fileCont = $line1 . "\n" . $line2 . "\n" . $line3 . "\n" . $line4 . "\n" . $line5 . "\n"
            . $line6;
            
        $file = $fileCont;
            
        file_put_contents($fileName, $file);
    }
    
}

?>
