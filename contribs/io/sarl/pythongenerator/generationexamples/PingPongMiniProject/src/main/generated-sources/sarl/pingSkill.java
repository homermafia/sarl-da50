import com.google.common.base.Objects;
import io.sarl.core.OpenEventSpace;
import io.sarl.lang.annotation.SarlElementType;
import io.sarl.lang.annotation.SarlSpecification;
import io.sarl.lang.annotation.SyntheticMember;
import io.sarl.lang.core.Address;
import io.sarl.lang.core.Event;
import io.sarl.lang.core.Scope;
import io.sarl.lang.core.Skill;
import io.sarl.lang.util.SerializableProxy;
import java.io.ObjectStreamException;
import org.eclipse.xtext.xbase.lib.InputOutput;
import org.eclipse.xtext.xbase.lib.Pure;

@SarlSpecification("0.12")
@SarlElementType(22)
@SuppressWarnings("all")
public class pingSkill extends Skill implements pingCapacity {
  private OpenEventSpace spc;
  
  public pingSkill(final OpenEventSpace pingSpace) {
    this.spc = pingSpace;
  }
  
  public void sendping() {
    int _numberOfStrongParticipants = this.spc.getNumberOfStrongParticipants();
    if ((_numberOfStrongParticipants > 1)) {
      PingEvent e = new PingEvent(0);
      InputOutput.<String>println("Sending ping event");
      this.spc.emit(this.getOwner().getID(), e, null);
    } else {
      InputOutput.<String>println("I am alone in this space");
    }
  }
  
  public void replyPing(final Event occ) {
    int _numberOfStrongParticipants = this.spc.getNumberOfStrongParticipants();
    if ((_numberOfStrongParticipants > 1)) {
      PingEvent e = new PingEvent(0);
      InputOutput.<String>println("Replying with ping event");
      class $SerializableClosureProxy implements Scope<Address> {
        
        private final Address $_source;
        
        public $SerializableClosureProxy(final Address $_source) {
          this.$_source = $_source;
        }
        
        @Override
        public boolean matches(final Address it) {
          return Objects.equal(it, $_source);
        }
      }
      final Scope<Address> _function = new Scope<Address>() {
        @Override
        public boolean matches(final Address it) {
          Address _source = occ.getSource();
          return Objects.equal(it, _source);
        }
        private Object writeReplace() throws ObjectStreamException {
          return new SerializableProxy($SerializableClosureProxy.class, occ.getSource());
        }
      };
      this.spc.emit(this.getOwner().getID(), e, _function);
    } else {
      InputOutput.<String>println("I am alone in this space");
    }
  }
  
  @Override
  @Pure
  @SyntheticMember
  public boolean equals(final Object obj) {
    return super.equals(obj);
  }
  
  @Override
  @Pure
  @SyntheticMember
  public int hashCode() {
    int result = super.hashCode();
    return result;
  }
}
