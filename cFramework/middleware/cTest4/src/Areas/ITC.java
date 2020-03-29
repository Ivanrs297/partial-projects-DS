package Areas;


import cFramework.nodes.area.Area;
import ctest4.IDs;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author armando-cinves
 */
public class ITC extends Area {
    
    public ITC(){
        this.ID = IDs.ITC;
        this.namer = IDs.class;
    }
    
    public void init(){ 
        send(IDs.ITC, "Message to me".getBytes());
    }
    
    

    @Override
    public void receive(long sender, byte[] data) {
        System.out.print(new String(data));
    }
    
}
