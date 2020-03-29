/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Area4;

import Area3.*;
import Area1.*;
import cFramework.communications.spikes.SpikeMerger;
import cFramework.communications.spikes.SpikeRouter;
import cFramework.nodes.area.Area;
import conf.Names;
import java.util.HashMap;

/**
 *
 * @author arman
 */
public class Area4 extends Area {
    
    public Area4(){
        this.ID = Names.Area4;
        this.namer = Names.class;
        addProcess(Process4.class);
        
        AddRoute(new SpikeRouter( 
            new long[]{Names.Process2,Names.Process3}, 
            new long[]{Names.Process4}, 
            new SpikeMerger() {
                public byte[] merge(HashMap<Long, byte[]> spikes) {
                    return "Ya mesclado".getBytes();
                }
        }));
    }
    
    @Override
    public void receive(long nodeID, byte[] data) {
    }
    
}