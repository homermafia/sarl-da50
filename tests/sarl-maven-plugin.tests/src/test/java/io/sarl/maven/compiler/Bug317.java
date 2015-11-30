/*
 * $Id$
 *
 * SARL is an general-purpose agent programming language.
 * More details on http://www.sarl.io
 *
 * Copyright (C) 2014-2015 the original authors or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package io.sarl.maven.compiler;

import static org.junit.Assert.assertNotNull;

import java.io.InputStream;
import java.net.URL;
import java.nio.file.FileSystems;
import java.nio.file.Path;

import org.apache.maven.it.Verifier;
import org.junit.Assume;
import org.junit.Before;
import org.junit.Ignore;
import org.junit.Test;

/**
 * @author $Author: sgalland$
 * @version $FullVersion$
 * @mavengroupid $GroupId$
 * @mavenartifactid $ArtifactId$
 */
@SuppressWarnings("all")
public class Bug317 extends AbstractMojoTest {

	@Before
	public void setUp() throws Exception {
		// The test can be run only of Janus is available.
		URL url = new URL("http://maven.janusproject.io/io.janusproject/io.janusproject.kernel/0.3.0-SNAPSHOT");
		try {
			InputStream inputStream = url.openStream();
			inputStream.close();
		} catch (Exception e) {
			Assume.assumeNoException(e);
		}
	}
	
	@Test
	@Ignore
	public void compile() throws Exception {
		Verifier verifier = executeMojo("prj3", "compile");
		Path path = FileSystems.getDefault().getPath(
				"src", "main", "generated-sources", "sarl",
				"io", "sarl", "maven", "compiler", "tests", "MyAgent.java");
		assertNotNull(path);
		verifier.assertFilePresent(path.toString());
	}
	
}