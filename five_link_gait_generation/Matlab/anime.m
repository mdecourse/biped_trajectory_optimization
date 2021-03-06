axis([-2 1 -1 2])

r01=[-l1*sin(x(1,:));l1*cos(x(1,:))];
r12=r01+[-l2*sin(x(2,:));l2*cos(x(2,:))];
r23=r12+[l3*sin(x(3,:));l3*cos(x(3,:))];
r24=r12+[l4*sin(x(4,:));-l4*cos(x(4,:))];
r45=r24+[l5*sin(x(5,:));-l5*cos(x(5,:))];
ground = line([-2 2],[0 0],'Color','m');
for i = 1:length(t)
    stance_t = line([0 r01(1,i)],[0 r01(2,i)],'Color','red');
    stance_f = line([r01(1,i) r12(1,i)],[r01(2,i) r12(2,i)],'Color','blue');
    torso = line([r12(1,i) r23(1,i)],[r12(2,i) r23(2,i)],'Color','green');
    swing_f = line([r12(1,i) r24(1,i)],[r12(2,i) r24(2,i)],'Color','yellow');
    swing_t = line([r24(1,i) r45(1,i)],[r24(2,i) r45(2,i)],'Color','black');
    
    pause(0.3)
    delete(stance_t)
    delete(swing_f)
    delete(swing_t)
    delete(stance_f)
    delete(torso)
end
