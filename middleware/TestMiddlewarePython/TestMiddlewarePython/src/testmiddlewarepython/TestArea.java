/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testmiddlewarepython;

import cFramework.nodes.area.Area;
import cFramework.nodes.process.ProcessConfiguration;
/**
 *
 * @author Luis Martin
 */
public class TestArea extends Area {

    public TestArea() {
        this.ID = AreaNames.TestArea;
        this.namer = AreaNames.class;
        addProcess("Test_1", ProcessConfiguration.LENG_PYTHON);
    }

    @Override
    public void init() {
        send(AreaNames.TestArea_1, "mesnaje".getBytes());
    }

    @Override
    public void receive(long nodeID, byte[] data) {
        log.message(new  String(data));
    }
}
