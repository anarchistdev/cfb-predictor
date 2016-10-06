<?php

class Team {
    public $wins;
    public $losses;
    public $conf;
    public $numInjuries = 0;
    public $rank; // AP poll
    public $sos; // sos - strength of schedule
    public $name;
    public $avgRushYds;
    public $avgDefRush;
    public $passCmp;
    public $passAtt;
    public $passYds;
    public $ppg;
    public $totalYds;
    
    
    public function export() {
        $fileName = "sets/" . $this->name . ".txt";
        $file = file_get_contents($fileName);
        $line1 = $this->wins;
        $line2 = $this->losses;
        $line3 = $this->conf;
        $line4 = $this->rank;
        $line5 = $this->sos;
        $line6 = $this->numInjuries;
        $line7 = $this->avgRushYds;
        $line8 = $this->avgDefRush;
        $line9 = $this->ppg;
        $line10 = $this->passCmp;
        $line11 = $this->passAtt;
        $line12 = $this->passYds;
        $line13 = $this->totalYds;

        $fileCont = $line1 . "\n" . $line2 . "\n" . $line3 . "\n" . $line4 . "\n" . $line5 . "\n"
            . $line6 . "\n" . $line7 . "\n" . $line8 . "\n" . $line9
             . "\n" . $line10 . "\n" . $line11 . "\n" . $line12 . "\n" . $line13;
            
        $file = $fileCont;
            
        file_put_contents($fileName, $file);
    }
    
}

?>
