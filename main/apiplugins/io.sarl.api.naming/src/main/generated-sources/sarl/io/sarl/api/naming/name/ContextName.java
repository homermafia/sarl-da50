/**
 * $Id$
 * 
 * SARL is an general-purpose agent programming language.
 * More details on http://www.sarl.io
 * 
 * Copyright (C) 2014-2020 the original authors or authors.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 * http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.sarl.api.naming.name;

import io.sarl.api.naming.name.SarlName;
import io.sarl.lang.annotation.PrivateAPI;
import io.sarl.lang.annotation.SarlElementType;
import io.sarl.lang.annotation.SarlSpecification;
import io.sarl.lang.annotation.SyntheticMember;
import java.net.URI;
import java.util.Objects;
import java.util.UUID;
import org.eclipse.xtend.lib.annotations.Accessors;
import org.eclipse.xtext.xbase.lib.Pure;

/**
 * This class represents a context name.
 * 
 * @author $Author: sgalland$
 * @version $FullVersion$
 * @mavengroupid $GroupId$
 * @mavenartifactid $ArtifactId$
 * @since 0.12
 */
@SarlSpecification("0.12")
@SarlElementType(10)
@SuppressWarnings("all")
public class ContextName extends SarlName {
  @Accessors
  private final UUID contextId;
  
  /**
   * Constructor.
   * 
   * @param uri the uri of the context.
   * @param contextId the identifier of the context.
   */
  @PrivateAPI
  public ContextName(final URI uri, final UUID contextId) {
    super(uri);
    this.contextId = contextId;
  }
  
  @Override
  @Pure
  @SyntheticMember
  public boolean equals(final Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    ContextName other = (ContextName) obj;
    if (!Objects.equals(this.contextId, other.contextId))
      return false;
    return super.equals(obj);
  }
  
  @Override
  @Pure
  @SyntheticMember
  public int hashCode() {
    int result = super.hashCode();
    final int prime = 31;
    result = prime * result + Objects.hashCode(this.contextId);
    return result;
  }
  
  @Override
  @Pure
  @SyntheticMember
  public ContextName clone() {
    try {
      return (ContextName) super.clone();
    } catch (Throwable exception) {
      throw new Error(exception);
    }
  }
  
  @SyntheticMember
  private static final long serialVersionUID = 601933167L;
  
  @Pure
  public UUID getContextId() {
    return this.contextId;
  }
}
