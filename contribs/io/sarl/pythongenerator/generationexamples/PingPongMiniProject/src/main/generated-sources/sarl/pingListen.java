import io.sarl.core.Destroy;
import io.sarl.core.Initialize;
import io.sarl.core.OpenEventSpace;
import io.sarl.lang.annotation.ImportedCapacityFeature;
import io.sarl.lang.annotation.PerceptGuardEvaluator;
import io.sarl.lang.annotation.SarlElementType;
import io.sarl.lang.annotation.SarlSpecification;
import io.sarl.lang.annotation.SyntheticMember;
import io.sarl.lang.core.Agent;
import io.sarl.lang.core.AtomicSkillReference;
import io.sarl.lang.core.Behavior;
import io.sarl.lang.core.Event;
import java.util.Collection;
import java.util.Set;
import org.eclipse.xtext.xbase.lib.Extension;
import org.eclipse.xtext.xbase.lib.InputOutput;
import org.eclipse.xtext.xbase.lib.Pure;

@SarlSpecification("0.12")
@SarlElementType(21)
@SuppressWarnings("all")
public class pingListen extends Behavior {
  public pingListen(final Agent owner, final OpenEventSpace spc) {
    super(owner);
  }
  
  private void $behaviorUnit$Initialize$0(final Initialize occurrence) {
  }
  
  private void $behaviorUnit$Destroy$1(final Destroy occurrence) {
  }
  
  private void $behaviorUnit$PingEvent$2(final PingEvent occurrence) {
    InputOutput.<String>println("Received ping event");
    pongCapacity _$CAPACITY_USE$PONGCAPACITY$CALLER = this.$CAPACITY_USE$PONGCAPACITY$CALLER();
    _$CAPACITY_USE$PONGCAPACITY$CALLER.replyPong(occurrence);
  }
  
  @Extension
  @ImportedCapacityFeature(pongCapacity.class)
  @SyntheticMember
  private transient AtomicSkillReference $CAPACITY_USE$PONGCAPACITY;
  
  @SyntheticMember
  @Pure
  private pongCapacity $CAPACITY_USE$PONGCAPACITY$CALLER() {
    if (this.$CAPACITY_USE$PONGCAPACITY == null || this.$CAPACITY_USE$PONGCAPACITY.get() == null) {
      this.$CAPACITY_USE$PONGCAPACITY = $getSkill(pongCapacity.class);
    }
    return $castSkill(pongCapacity.class, this.$CAPACITY_USE$PONGCAPACITY);
  }
  
  @SyntheticMember
  @PerceptGuardEvaluator
  private void $guardEvaluator$Initialize(final Initialize occurrence, final Collection<Runnable> ___SARLlocal_runnableCollection) {
    assert occurrence != null;
    assert ___SARLlocal_runnableCollection != null;
    ___SARLlocal_runnableCollection.add(() -> $behaviorUnit$Initialize$0(occurrence));
  }
  
  @SyntheticMember
  @PerceptGuardEvaluator
  private void $guardEvaluator$Destroy(final Destroy occurrence, final Collection<Runnable> ___SARLlocal_runnableCollection) {
    assert occurrence != null;
    assert ___SARLlocal_runnableCollection != null;
    ___SARLlocal_runnableCollection.add(() -> $behaviorUnit$Destroy$1(occurrence));
  }
  
  @SyntheticMember
  @PerceptGuardEvaluator
  private void $guardEvaluator$PingEvent(final PingEvent occurrence, final Collection<Runnable> ___SARLlocal_runnableCollection) {
    assert occurrence != null;
    assert ___SARLlocal_runnableCollection != null;
    ___SARLlocal_runnableCollection.add(() -> $behaviorUnit$PingEvent$2(occurrence));
  }
  
  @SyntheticMember
  @Override
  public void $getSupportedEvents(final Set<Class<? extends Event>> toBeFilled) {
    super.$getSupportedEvents(toBeFilled);
    toBeFilled.add(PingEvent.class);
    toBeFilled.add(Destroy.class);
    toBeFilled.add(Initialize.class);
  }
  
  @SyntheticMember
  @Override
  public boolean $isSupportedEvent(final Class<? extends Event> event) {
    if (PingEvent.class.isAssignableFrom(event)) {
      return true;
    }
    if (Destroy.class.isAssignableFrom(event)) {
      return true;
    }
    if (Initialize.class.isAssignableFrom(event)) {
      return true;
    }
    return false;
  }
  
  @SyntheticMember
  @Override
  public void $evaluateBehaviorGuards(final Object event, final Collection<Runnable> callbacks) {
    super.$evaluateBehaviorGuards(event, callbacks);
    if (event instanceof PingEvent) {
      final PingEvent occurrence = (PingEvent) event;
      $guardEvaluator$PingEvent(occurrence, callbacks);
    }
    if (event instanceof Destroy) {
      final Destroy occurrence = (Destroy) event;
      $guardEvaluator$Destroy(occurrence, callbacks);
    }
    if (event instanceof Initialize) {
      final Initialize occurrence = (Initialize) event;
      $guardEvaluator$Initialize(occurrence, callbacks);
    }
  }
}
