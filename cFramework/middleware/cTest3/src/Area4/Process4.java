/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area4;

import Area3.*;
import Area1.*;
import conf.Names;

/**
 *
 * @author arman
 */
public class Process4 extends cFramework.nodes.process.Process {
    
    public Process4 () {
        this.ID = Names.Process4;
        this.namer = Names.class;
    }

    @Override
    public void receive(long nodeID, byte[] data) {
        log.message("Recibido Proceso 4");
        log.message( this.currentMetadata.time + " "+ new String(data) );
    }
    
}
